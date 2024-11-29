import collections

def firstUniqChar(s):
    count = collections.Counter(s)
        
    for index in range(len(s)):
        if count[s[index]] == 1:
            return index
    return -1