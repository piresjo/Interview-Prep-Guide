def merge(arrA, arrB, lastA, lastB):
    if not arrA:
        return None
    if not arrB:
        return arrA
    indexA = lastA - 1
    indexB = lastB - 1
    indexMerged = lastB + lastA - 1

    while indexB >= 0:
        if indexA >= 0 and arrA[indexA] > arrB[indexB]:
            arrA[indexMerged] = arrA[indexA]
            indexA -= 1
        else:
            arrA[indexMerged] = arrB[indexB]
            indexB -= 1
        indexMerged -= 1
    return arrA

    