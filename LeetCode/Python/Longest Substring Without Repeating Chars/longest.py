def lengthOfLongestSubstring(s):
    lenVal = len(s)
    setVal = set()
    returnLen = 0
    left = 0
    right = 0
    while (left < lenVal and right < lenVal):
        if s[right] not in setVal:
            setVal.add(s[right])
            right += 1
            returnLen = max(returnLen, right - left)
        else:
            setVal.remove(s[left])
            left += 1
    return returnLen