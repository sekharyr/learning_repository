#stack pr tool
import argparse
import json
import subprocess
import os
from github import Github

#Fixing as per review comment
#One more additon

#one more addtion - two


# Authentication

token = os.getenv("GITHUB_TOKEN")  # GitHub token from environment variables
if not token:
    raise ValueError("GITHUB_TOKEN environment variable not set.")
g = Github(token)
# Auth1

# Repository details env variable
repo_name = os.getenv("GITHUB_REPO")  # Repository name from environment variables
if not repo_name:
    raise ValueError("GITHUB_REPO environment variable not set.")
repo = g.get_repo(repo_name)

# File to persist dependency graph
dependency_file = "dependency_graph.json"

# Load dependency graph from file
def load_dependency_graph():
    try:
        with open(dependency_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save dependency graph to file
def save_dependency_graph(graph):
    with open(dependency_file, "w") as f:
        json.dump(graph, f, indent=4)

# Initialize dependency graph
dependency_graph = load_dependency_graph()

# Create a new branch and commit
def create_branch_and_commit(branch_name, commit_message):
    subprocess.run(["git", "checkout", "-b", branch_name])
    subprocess.run(["git", "commit", "-m", commit_message])
    subprocess.run(["git", "push", "--set-upstream", "origin", branch_name])
    print(f"Branch {branch_name} created, changes committed, and pushed to remote.")


# Generate linked PR information
def generate_linked_pr_info(branch):
    parent_branch = dependency_graph.get(branch, {}).get("parent")
    if parent_branch:
        return f"This PR is stacked on top of {parent_branch}."
    return ""

# Create a pull request
def create_pr(branch, base, title, body):
    # Determine the parent branch before creating the PR
    subprocess.run(["git", "checkout", base])
    parent_branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).strip().decode()

    # Update the dependency graph with parent information
    dependency_graph[branch] = {"parent": parent_branch}
    save_dependency_graph(dependency_graph)

    # Generate linked PR information
    linked_info = generate_linked_pr_info(branch)
    full_body = f"{body}\n\n{linked_info}"
    subprocess.run(["git", "checkout", branch])
    # Ensure the branch is pushed to the remote
    subprocess.run(["git", "push", "--set-upstream", "origin", branch])
    # Create the pull request
    pr = repo.create_pull(
        title=title,
        body=full_body,
        head=branch,
        base=base,
    )
    
    # Save PR number to the dependency graph
    dependency_graph[branch]["pr_number"] = pr.number
    save_dependency_graph(dependency_graph)
    print(f"Pull request created: {pr.html_url}")
    return pr


# Recursively rebase child branches using update-refs
def rebase_children(branch):
    for child, data in dependency_graph.items():
        if data.get("parent") == branch:
            subprocess.run(["git", "checkout", "-b", child])
            print(f"Rebasing child branch: {child} onto {branch}")
            # subprocess.run(["git", "update-ref", f"refs/heads/{child}", f"refs/heads/{branch}"])
            subprocess.run(["git", "rebase", branch])
            print(f"Rebased {child} onto {branch}.")
            subprocess.run(["git", "push", "--set-upstream", "origin", child])
            rebase_children(child)  # Recursively rebase further children

# Restack branches and update PR dependencies
def restack_branches(base_branch):
    subprocess.run(["git", "rebase", base_branch])
    print(f"Branches restacked on {base_branch}.")
    rebase_children(base_branch)

# Submit PRs for all branches in the stack
def submit_prs():
    for child, data in dependency_graph.items():
        pr = repo.get_pull(data.get("pr_number"))
        linked_info = generate_linked_pr_info(child)
        pr.edit(body=f"{pr.body}\n\n{linked_info}")  # Update PR with linked information
        pr.create_review_request()  # Submit PR
        print(f"Submitted PR #{data.get('pr_number')}: {pr.html_url}")

# Check for conflicts and ensure a clean state
def check_conflicts():
    for child, data in dependency_graph.items():
        pr = repo.get_pull(data.get("pr_number"))
        if pr.mergeable_state != "clean":
            print(f"Conflict detected in PR #{data.get('pr_number')}. Please resolve conflicts.")

# Display the dependency graph as a tree
def display_tree(branch, level=0):
    pr_number = dependency_graph.get(branch, {}).get("pr_number")
    pr_info = f" (PR #{pr_number})" if pr_number else ""
    print("  " * level + f"- {branch}{pr_info}")
    for child, data in dependency_graph.items():
        if data.get("parent") == branch:
            display_tree(child, level + 1)

# Command-line interface
def main():
    parser = argparse.ArgumentParser(description="Manage stacked pull requests with branch automation.")
    parser.add_argument("command", choices=["create", "modify", "submit", "check", "rebase", "view"], help="Command to execute")
    parser.add_argument("--branch", help="Branch name for create/modify/rebase commands")
    parser.add_argument("--message", help="Commit message for create commands")
    parser.add_argument("--base", default="main", help="Base branch for stacking or submission")
    args = parser.parse_args()

    if args.command == "create" and args.branch and args.message:
        create_branch_and_commit(args.branch, args.message)
        create_pr(args.branch, args.base, args.message, "")
    elif args.command == "modify" and args.branch and args.message:
        subprocess.run(["git", "checkout", args.branch])
        subprocess.run(["git", "commit", "-m", args.message])
        subprocess.run(["git", "push", "--set-upstream", "origin", args.branch])
        rebase_children(args.branch)
    elif args.command == "submit":
        submit_prs()
    elif args.command == "check":
        check_conflicts()
    elif args.command == "rebase" and args.branch:
        rebase_children(args.branch)
    elif args.command == "view":
        print("Pull Request Dependency Tree:")
        display_tree("master")
    else:
        print("Invalid command or missing arguments.")

if __name__ == "__main__":
    main()
