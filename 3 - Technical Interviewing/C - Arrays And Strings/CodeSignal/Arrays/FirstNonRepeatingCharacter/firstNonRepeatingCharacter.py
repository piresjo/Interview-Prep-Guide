def firstNotRepeatingCharacter(s):
    charDict = {}
    for x in s:
        if x not in charDict:
            charDict[x] = 1
        else:
            charDict[x] += 1

    for x in s:
        if charDict[x] == 1:
            return x
    return "_"
