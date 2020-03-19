#syntax : filter(func,iterables)


#implementation of map using lambda
#program 1
n = [4,3,2,1]
print(list(filter(lambda x: x>2 ,n)))


#implementation of map using normal function
#program 2
def new1(i):
    if i>=3:
        return i
j=filter(new1,(1,2,3,4,5,6,7))
print(j)  #object of filter
print(tuple(j))