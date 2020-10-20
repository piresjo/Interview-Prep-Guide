def replaceSpaces(strVal):
    if strVal is None:
        return None
    returnString = ""
    strVal = strVal.strip()
    for char in strVal:
        if char == " ":
            returnString += "%20"
        else:
            returnString += char
    return returnString