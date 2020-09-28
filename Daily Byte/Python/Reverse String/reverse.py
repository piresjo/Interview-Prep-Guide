def reverse(strVal):
    if not strVal:
        return ""
    returnVal = ""
    for i in range(len(strVal)-1, -1, -1):
        returnVal += strVal[i]
    return returnVal