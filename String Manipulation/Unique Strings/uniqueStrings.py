# We can use extra memory
def allUniqueChars(str1):
    charDict = {}
    for x in str1:
        if x in charDict:
            charDict[x] += 1
        else:
            charDict[x] = 1
    for k, v in charDict:
        if v > 1:
            return False
    return True

# We can't use extra memory
# Assume that python's internal string sort is using quicksort, which uses little memory
# Runtime will be O(nln(n))
def allUniqueCharsNoMemory(str1):
    str1 = str1.sort()
    for i in range(0, len(str1) - 2):
        if str1[i] == str1[i + 1]:
            return False
    return True

    
