def minRemoveToMakeValid(s):
    temp = ""
    openVal = 0       
    for char in s:
        if char == '(':
            openVal += 1
        elif char == ')':
            if openVal == 0:
                continue
            openVal -= 1
        temp += char
    result = ""
    for i in range(len(temp)-1, -1, -1):
        if temp[i] == '(' and (openVal-1) >= 0:
            openVal -= 1
            continue
        result += temp[i]
    return result[::-1]