from heapq import *


def reorganizeString(S):
    charMap = {}
    for char in S:
        if char not in charMap:
            charMap[char] = 1
        else:
            charMap[char] += 1

    heap = []
    for char in charMap.keys():
        heappush(heap, (charMap[char] * -1, char))

    returnVal = ""
    while len(heap) > 1:
        currVal = heappop(heap)
        nextVal = heappop(heap)

        returnVal += currVal[1]
        returnVal += nextVal[1]

        charMap[currVal[1]] -= 1
        charMap[nextVal[1]] -= 1

        if charMap[currVal[1]] > 0:
            heappush(heap, (currVal[0] + 1, currVal[1]))
        if charMap[nextVal[1]] > 0:
            heappush(heap, (nextVal[0] + 1, nextVal[1]))

    if len(heap) > 0:
        last = heappop(heap)
        if charMap[last[1]] > 1:
            return ""
        else:
            returnVal += last[1]
    return returnVal
