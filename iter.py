from itertools import combinations
from itertools import permutations
from itertools import product
import itertools
# program 1
count = 0

for i in itertools.cycle('AB'):
    if count > 7:
        break
    else:
        print(i, end=" ")
        count += 1
# Program2
print("\nThe cartesian product using repeat:")
print(list(product([1, 2], repeat=2)))
print("The cartesian product of the containers:")
print(list(product('AB', [3, 4])))

# Program 3
print("All the permutations of the given string is:")
print(list(permutations('AB')))
print()
print("All the permutations of the given container is:")
print(list(permutations(range(3), 2)))


# Program 4

print("All the combination of list in sorted order(without replacement) is:")
print(list(combinations(['A', 2], 2)))
print()

print("All the combination of string in sorted order(without replacement) is:")
print(list(combinations('AB', 2)))
print()
