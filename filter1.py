tensilestrengthofsteelinMPA=[500,650,700,100,200,350,685]
def approvedsteel(n):
    if(n<650):
        return true
    else:
        return false
a=filter(approvedsteel,tensilestrengthofsteelinMPA)
for i in a:
    print(i+"is better steel")
