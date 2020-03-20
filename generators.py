#generators

#program 1
def new(dict):
    for x ,y in dict.items():
        yield x,y
a= {1:"hi", 2:"welcome"}
b=new(a)  #geneators object
print(b)
print(next(b))
print(next(b))

#program 2
#generators with loops
def ex():
    n=3
    yield n
    n=n*n
    yield n
v= ex()
for x in v:
    print(x)

#program 3
#generators expression
f= range(6)
print("List comp" ,end=":")
q=[x+2 for x in f]
print(q)
print("gen comp" ,end=":")
r=(x+2 for x in f)
print(r)  #genrator object
for x in r:
    print(x)



