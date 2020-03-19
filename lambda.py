
#program 1
#lambda without using user defined funation
mx = lambda x,y :x if x>y else  y
print(mx(8,5))

#program2
#lambda with user defined function
def A(x):
    return(lambda y :x + y )
t=A(4)
u=A(5)
print(t(8))
print(u(5))