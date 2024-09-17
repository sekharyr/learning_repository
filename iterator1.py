import itertools

# for in loop
for i in itertools.count(0, 2):
    if i == 100:
        break
    else:
        print(i)