#syntax : map(func,iterables)


#implementation of map using lambda
#program 1
n = [4,3,2,1]
print(list(map(lambda x:x**2,n)))


#implementation of map using normal function
#program 2
def new(a,b):
    return a*b
x=map(new,[1,2,3,4],[2,3,4,5])
print(x)  #object of map
print(tuple(x))

