
#function to return odd numbers
def example1(num):
    return num%2

#functions to return vowels
def example2(s):
    v=['a','e','i','o','u']
    return s in v

def filterDemo():
    list1=[2,5,6,3,8,9,1]
    result1=filter(example1,list1)
    print(list(result1))
    list2=['a','w','q','e','f']
    result2=filter(example2,list2)
    print(list(result2))

if __name__ == "__main__":
    filterDemo()