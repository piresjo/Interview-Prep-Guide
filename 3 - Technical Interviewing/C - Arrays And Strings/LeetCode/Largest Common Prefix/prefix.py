"""
The prefix is the first n letters of the string
(at most n is the length of the smallest string in the array).

Once we find out what the max n value is, we scan through the first
n characters of the strings. If str[i][j] != str[i-1][j], we return the
prefix we have. Otherwise, we add to the prefix return val.
"""


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
            if strs[j][i] != strs[j - 1][i]:
                return returnString
        returnString += strs[0][i]
    return returnString
