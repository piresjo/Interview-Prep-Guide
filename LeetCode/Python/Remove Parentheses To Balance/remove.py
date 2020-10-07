''' 
    General Idea: You have to make two passes to deal with two different
    cases: too many open parentheses and too many closed parentheses.

    The first path deals with closes parentheses. We create a temp string that'll
    give us the string with all the closed parentheses we need. Keep count of 
    open parentheses, so when you encounter a closed parenthesis, you can determine
    whether or not to add that parenthesis.

    However, you might still have excess open parentheses. So, you'll have to
    make another pass through the list, this time backwards. Create the returnString
    (we'll return the reverse of this string) and as we go along, if we still have 
    an openVal greater than 0, we don't add open parentheses until openVal becomes 0
'''

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