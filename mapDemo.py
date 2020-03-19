from math import sqrt
from random import sample

#function return cube of squreroot of given squre number
def example1(num):
    print(num,end=' --> ')
    return int(sqrt(num)*num)


#function return multiplication of squre root of given squere numbers
def example2(a,b):
    print(a,b,end=' --> ')
    return int(sqrt(a)*sqrt(b))


# demo function for map
def demoMap():
    list1=[4,9,16,25,36,49,64,81,100]
    result1=map(example1,list1)
    print("example1......")
    for result in result1:
        print(result)
    print("example2.....")
    result2=map(example2,list1,sample(list1,len(list1)))   #sample returns shuffeled list parm-list,len of list to be returned
    for result in result2:
        print(result)

if __name__ == "__main__":
    demoMap()