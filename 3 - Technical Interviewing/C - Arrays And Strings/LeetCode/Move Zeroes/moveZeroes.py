from typing import List


def moveZeroes(nums: List[int]) -> None:
    nextNonZero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[nextNonZero], nums[i] = nums[i], nums[nextNonZero]
            nextNonZero += 1
    return nums