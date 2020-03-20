dictOfNames = {
    7: 'sam',
    8: 'john',
    9: 'mathew',
    10: 'riti',
    11: 'aadi',
    12: 'sachin'
}

newDict = dict(filter(lambda elem: elem[0] % 2 == 0, dictOfNames.items()))

print('Filtered Dictionary : ')
print(newDict)
# Program 2
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print(list(Fahrenheit))
