nums = [21, 19, 18, 46, 6, 29]
def checkPrime(num):
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                return true
                break
        else:
            return true


    else:
        return false

data = filter(checkPrime, nums)
print(list(data))