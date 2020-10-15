def uncommon(str1, str2):
    str1List = str1.split()
    str2List = str2.split()

    wordDict = {}
    for word in str1List:
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] += 1

    for word in str2List:
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] += 1

    returnList = []
    for word in wordDict.keys():
        if wordDict[word] == 1:
            returnList.append(word)
    
    return returnList
