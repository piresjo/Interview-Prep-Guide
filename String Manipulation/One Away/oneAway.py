def populateDict(str, dictVal):
    for x in str:
        if x in dictVal:
            dictVal[x] += 1
        else:
            dictVal[x] = 1
    return dictVal


def oneAwayOrLess(str1, str2):
    # Return false if dealing with null strings
    if str1 is None or str2 is None:
        return False
    
    if str1 == str2:
        return True

    if abs(len(str1) - len(str2)) > 1:
        return False
    
    str1Dict = populateDict(str1, {})
    str2Dict = populateDict(str2, {})

    biggerDict = None
    smallerDict = None

    if abs(len(str1))- abs(len(str2)) == 1:
        biggerDict = str1Dict if (len(str1) > len(str2)) else str2
        smallerDict =  str1Dict if (len(str1) < len(str2)) else str2
    else:
        biggerDict = str1Dict
        smallerDict = str2Dict

    numIncorrect = 0

    for k, v in biggerDict:
        if k not in smallerDict:
            numIncorrect += 1
        else:
            numIncorrect += (v - smallerDict[k])
        if numIncorrect > 1:
            return False
    return True


    