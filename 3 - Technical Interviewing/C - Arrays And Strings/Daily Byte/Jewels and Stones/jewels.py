def numJewels(jewels, stones):
    returnNum = 0
    for char in stones:
        if char in jewels:
            returnNum += 1
    return returnNum