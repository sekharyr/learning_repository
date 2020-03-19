def fibnum(limit): 
    a=0
    b=1
    while a < limit: 
        yield a 
        a, b = b, a + b 

def powFun(limit,p):
    n=1
    while n < limit:
        yield pow(n,p)
        n+=1


def generator():
    print("function 1 ......")
    fun1=fibnum(100)
    # print(list(fibnum(5)))
    for _ in range(10):
        print(fun1.__next__())
    print("power function")
    fun2=powFun(1001,3)
    for _ in range(10):
        print(fun2.__next__())


if __name__ == "__main__":
    generator()