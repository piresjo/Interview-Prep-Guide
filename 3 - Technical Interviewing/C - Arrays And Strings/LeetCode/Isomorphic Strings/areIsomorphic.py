def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    sDict = {}
    tDict = {}

    for i in range(len(s)):
        if s[i] not in sDict:
            sDict[s[i]] = i

        if t[i] not in tDict:
            tDict[t[i]] = i

        if sDict[s[i]] != tDict[t[i]]:
            return False

    return True
