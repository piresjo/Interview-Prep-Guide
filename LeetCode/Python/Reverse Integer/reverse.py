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