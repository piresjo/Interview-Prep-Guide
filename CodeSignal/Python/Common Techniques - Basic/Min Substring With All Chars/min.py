from collections import Counter

def minSubstringWithAllChars(s, t):
    if not s or not t:
        return ""
    tDict = Counter(t)
    required = len(tDict)
    left = 0
    right = 0
        
    formed = 0
    windowCounts = {}
        
    ans = (float("inf"), None, None)
        
    while right < len(s):
        charVal = s[right]
        windowCounts[charVal] = windowCounts.get(charVal, 0) + 1
            
        if charVal in tDict and windowCounts[charVal] == tDict[charVal]:
            formed += 1
            
        while left <= right and formed == required:
            charVal = s[left]
                
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
                
            windowCounts[charVal] -= 1
            if charVal in tDict and windowCounts[charVal] < tDict[charVal]:
                formed -= 1
                    
            left += 1
            
        right += 1
        
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]