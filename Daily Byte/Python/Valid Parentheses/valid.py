def isValid(s):
    charStack = []
    for char in s:
        if char == '(' or char == '[' or char == '{':
            charStack.append(char)
        else:
            if len(charStack) == 0:
                return False
            popVal = charStack.pop()
            if popVal == '(' and char != ')':
                return False
            if popVal == '[' and char != ']':
                return False
            if popVal == '{' and char != '}':
                return False
    return len(charStack) == 0