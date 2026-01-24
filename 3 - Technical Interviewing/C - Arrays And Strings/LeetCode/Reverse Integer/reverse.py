def reverse(x):
    valAsString = str(x)
    newNumber = ""
    makeNegative = False
    for i in range(len(valAsString)-1, -1, -1):
        if valAsString[i] == '-':
            makeNegative = True
        else:
            newNumber += valAsString[i]
        
    returnVal = int(newNumber)
    if makeNegative:
        returnVal *= -1
        
    if returnVal > ((2 ** 31) - 1) or returnVal < (-(2**31)):
        return 0
    
    return returnVal

def reverseMethod2(x):
    negative = False
    if x < 0:
        negative = True
        x *= -1

    reversedVal = 0  

    while x > 0:
        reversedVal = (reversedVal * 10) + (x % 10)
        x //= 10
        
    if reversedVal < (-2 ** 31) or reversedVal > ((2 ** 31) - 1):
        return 0
        
    if negative:
        return reversedVal * -1
        
    return reversedVal