# Prog

ages = [5, 12, 17, 18, 24, 32]


def myFunc(x):
    if x < 18:
        return False
    else:
        return True


adults = filter(myFunc, ages)

for x in adults:
    print(x)

# Program 2
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels


def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False


filteredVowels = filter(filterVowels, alphabets)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)
