def checkoddeven(n):
    if n%2==0:
       yield 1
    if n%2==1:
        yield 2




for value in checkoddeven(v):
    if(v==1):
        print('even')
    if (v == 2):
        print('odd')