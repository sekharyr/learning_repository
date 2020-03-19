from itertools import combinations,permutations,cycle

def combination(n,p):
    return list(combinations(range(n),p))
def permitaion(n,p):
    return list(permutations(range(n),p))


if __name__ == "__main__":
    # name=['krishna','ram','sham','raghu']
    name=cycle(['krishna','ram','sham','raghu'])
    for _ in range(10):
        print(name.__next__())
    com=combination(5,3)
    print('Total Combination = ',len(com),"\n",com)
    per=permitaion(4,3)
    print("Total Permutation = ",len(per),"\n",per)