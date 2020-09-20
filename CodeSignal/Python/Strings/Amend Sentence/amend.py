def amendTheSentence(s):
    if not s:
        return ""
    returnString = ""
    for i in range(0, len(s)):
        if s[i].lower() != s[i] and i == 0:
            returnString += s[i].lower()
            continue
        if s[i].lower() != s[i] and i != 0:
            returnString += " " + s[i].lower()
        else:
            returnString += s[i]
        
    return returnString