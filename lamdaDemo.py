from math import sqrt
from random import sample


# demo function for lambda
def demoLambda():
    list1=[4,9,16,25,36,49,64,81,100]
    print("example1....",list1)  #function return cube of squreroot of given squre number
    result1=map(lambda num: int(sqrt(num)*num),list1)
    for result in result1:
        print(result)
    list2=sample(list1,len(list1))
    print("example2.....",list1,list2)   #multiplication of squre root of given squere numbers
    result2=map(lambda a,b: int(sqrt(a)*sqrt(b)),list1,list2)   #sample returns shuffeled list parm-list,len of list to be returned
    for result in result2:
        print(result)

if __name__ == "__main__":
    demoLambda()