def reverseVowels(s: str) -> str:
    stringList = list(s)
    start = 0
    end = len(s) - 1
    vowels = ['a', 'e', 'i', 'o', 'u']

    while start < end:
        if stringList[start].lower() in vowels and stringList[end].lower() in vowels:
            stringList[start], stringList[end] = stringList[end], stringList[start]
            start += 1
            end -= 1
        else:
            if stringList[start].lower() not in vowels:
                start += 1
            if stringList[end].lower() not in vowels:
                end -= 1
    return "".join(stringList)