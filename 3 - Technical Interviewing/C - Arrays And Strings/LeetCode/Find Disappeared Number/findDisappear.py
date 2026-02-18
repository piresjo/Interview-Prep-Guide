from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        flipIndex = abs(nums[i]) - 1

        if nums[flipIndex] > 0:
            nums[flipIndex] *= -1

    res = []

    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i + 1)

    return res


def findDisappearedNumbersAlt(nums: List[int]) -> List[int]:
    numDict = {}
    for i in range(len(nums)):
        numDict[i + 1] = 0

    for num in nums:
        numDict[num] += 1

    res = []

    for key, val in numDict.items():
        if val == 0:
            res.append(key)

    return res
