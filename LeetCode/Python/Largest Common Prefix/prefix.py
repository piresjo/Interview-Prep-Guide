def longestCommonPrefix(strs):
    if not strs or len(strs) == 0:
        return ""
    minLen = float("inf")
    for stringVal in strs:
        if len(stringVal) < minLen:
            minLen = len(stringVal)
        
    returnString = ""
    for i in range(0, minLen):
        for j in range(1, len(strs)):
            if strs[j][i] != strs[j-1][i]:
                return returnString
        returnString += strs[0][i]
    return returnString