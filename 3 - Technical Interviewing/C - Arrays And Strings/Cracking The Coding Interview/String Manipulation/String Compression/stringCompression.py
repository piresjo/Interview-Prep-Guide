def compress(stringVal):
    if not stringVal:
        return stringVal

    if len(stringVal) == 0:
        return stringVal

    if not needToCompress(stringVal):
        return stringVal

    compressed = ""
    countConsecutive = 0

    for i in range(0, len(stringVal)):
        countConsecutive += 1

        if (i + 1) >= len(stringVal) or stringVal[i] != stringVal[i + 1]:
            compressed += stringVal[i]
            compressed += str(countConsecutive)
            countConsecutive = 0
    return compressed


def needToCompress(stringVal):
    setVal = set()
    for x in stringVal:
        setVal.add(x)
    return len(setVal) != len(stringVal)
