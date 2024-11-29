def areFollowingPatterns(strings, patterns):
    # Sanity check. If lengths are different, 
    if len(strings) != len(patterns):
        return False
        
    # need to map patterns to strings
    # we also need to ensure that we're not double counting strings, hence the set
    patternDict = {}
    stringSet = set()
    
    for i in range(0, len(strings)):
        if patterns[i] not in patternDict:
            # add to pattern dict, if string wasn't already used (and therefore would be in set)
            if strings[i] in stringSet:
                return False
            patternDict[patterns[i]] = strings[i]
        else:
            # if in pattern dict, verify that the dict val matches the string val
            if patternDict[patterns[i]] != strings[i]:
                return False
        stringSet.add(strings[i])
    return True

