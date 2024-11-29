def populateDict(str, dictVal):
    for x in str:
        if x in dictVal:
            dictVal[x] += 1
        else:
            dictVal[x] = 1
    return dictVal

def permOfPalindrome(str):
    if str is None:
        return False

    isEvenLen = (len(str) % 2 == 0)
    oddCountMax = 0 if isEvenLen else 1
    oddCount = 0

    strDict = populateDict(str, {})

    print(strDict)

    for k in strDict:
        if (strDict[k] % 2 != 0):
            oddCount += 1
            if oddCount > oddCountMax:
                return False
    return True
