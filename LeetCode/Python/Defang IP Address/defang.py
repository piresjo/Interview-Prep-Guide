'''
    General Idea: This is a simple pass through. In one pass, we can
    construct a new string to return. If not a period, we can just add the
    character, otherwise we add '[.]'
'''

def defangIPaddr(address: str) -> str:
    returnString = ""
    for char in address:
        if char == '.':
            returnString += '[.]'
        else:
            returnString += char
    return returnString