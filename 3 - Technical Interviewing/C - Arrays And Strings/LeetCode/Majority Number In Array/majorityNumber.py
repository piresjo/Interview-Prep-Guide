from typing import List


def majorityElement(nums: List[int]) -> int:
    elementDict = {}

    for num in nums:
        if num not in elementDict:
            elementDict[num] = 1
        else:
            elementDict[num] += 1

    halfN = len(nums) / 2
    returnVal = None

    for k, v in elementDict.items():
        if v > halfN:
            returnVal = k

    return returnVal
