from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        midpoint = (l + r) // 2

        if nums[midpoint] == target:
            return midpoint

        if nums[midpoint] > target:
            r = midpoint - 1
        else:
            l = midpoint + 1

    return l
