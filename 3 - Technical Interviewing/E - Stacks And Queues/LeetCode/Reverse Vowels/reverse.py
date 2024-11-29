'''
    General idea: for the reversing, use a stack for the vowels.
    Make two passes with the string. The first pass is to push the
    vowels into the stack. The second pass is to recreate the string.
    If not vowel, just add that character; otherwise, pop the value from
    the stack and add it to the returnString.
'''

def reverseVowels(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowelStack = []
    for char in s:
        if char.lower() in vowels:
            vowelStack.append(char)
    returnString = ""
    for i in range(0, len(s)):
        if s[i].lower() in vowels:
            returnString += vowelStack.pop()
        else:
            returnString += s[i]
        
    return returnString