def decodeString(s):
    stack = []
    stack.append([""])
    numString = ""

    for x in s:
        if x.isdigit():
            numString += x
        elif x == "[":
            stack.append(["", int(numString)])
            numString = ""
        elif x == "]":
            stringVal, repeatVal = stack.pop()
            stack[-1][0] += stringVal * repeatVal
        else:
            stack[-1][0] += x
    return stack[-1][0]
