# Program1
import random


def temp(celsius):
    for i in celsius:
        yield((float(9)/5)*i + 32)


celsius = [39.2, 36.5, 37.3, 37.8]

x = temp(celsius)
for i in x:
    print(i)

# Program2


def lottery():
    for i in range(6):
        yield random.randint(1, 40)

    yield random.randint(1, 15)


for random_number in lottery():
    print("And the next number is... %d!" % (random_number))
