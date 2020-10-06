def defangIPaddr(address: str) -> str:
    returnString = ""
    for char in address:
        if char == '.':
            returnString += '[.]'
        else:
            returnString += char
    return returnString