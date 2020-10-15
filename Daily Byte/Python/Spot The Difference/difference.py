def difference(str1, str2):
    charDict1 = {}
    for char in str1:
        if char not in charDict1:
            charDict1[char] = 1
        else:
            charDict1[char] += 1

    for char in str2:
        if char not in charDict1:
            return char
    
    return ''
