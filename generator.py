def factorial(n):
    if n == 1:
        yield 1
    else:
        yield n * factorial(n-1)

n=input('enter to be factored number')
fact=factorial(n)