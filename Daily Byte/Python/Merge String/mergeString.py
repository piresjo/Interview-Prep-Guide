def mergeString(s, t):
    mergeString = ""
    maxStringLen = max(len(s), len(t))

    for i in range(0, maxStringLen):
        if i < len(s):
            mergeString += s[i]
        if i < len(t):
            mergeString += t[i]
    
    return mergeString