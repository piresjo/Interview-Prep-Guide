def populateDict(str, dictVal):
    for x in str:
        if x in dictVal:
            dictVal[x] += 1
        else:
            dictVal[x] = 1
    return dictVal

def isPerm(str1, str2):
    if str1 is None or str2 is None:
        return False

    if len(str1) != len(str2):
        return False
    
    str1Dict = populateDict(str1, {})
    str2Dict = populateDict(str2, {})

    return str1Dict == str2Dict