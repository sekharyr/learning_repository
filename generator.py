from itertools import count

def fibnum(): 
    a,b=0,1
    # b=1
    while True:
        yield a 
        a, b = b, a + b 

def powFun(p):
    n=1
    while True:
        yield pow(n,p)
        n+=1


def generator():
    print("function 1 ......")
    fun1=fibnum()
    # print(list(fibnum(5)))
    for _ in range(10):
        print(fun1.__next__())    # OR print(next(fun2))
    print("power function")
    # fun2=powFun(3)         #OR  line above for loop(28)
    # x=count()
    # print(next(x))
    # print(next(x))
    fun2=(pow(a,3) for a in count())        # it replace the poeFun function , count is used to set range to infinity
    # print(dir(fun2))  #print possible inbuilt functions
    for _ in range(11):
        # print(fun2.__next__())    # OR
        print(next(fun2))


if __name__ == "__main__":
    generator()