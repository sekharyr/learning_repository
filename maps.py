from random import shuffle

# String shuffle


def jumble(words):
    anagram = list(words)
    shuffle(anagram)
    return ''.join(anagram)


words = ['varun', 'mahaveer', 'krishna', 'swaghath']

print(list(map(jumble, words)))

# program 2 string rev


def reverse(words):
    return words[::-1]


print(list(map(reverse, words)))
