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