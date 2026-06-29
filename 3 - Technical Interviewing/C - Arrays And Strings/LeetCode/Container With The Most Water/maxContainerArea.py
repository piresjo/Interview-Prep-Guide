from typing import List


def maxArea(height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        returnVal = 0

        while i < j:
            area = (min(height[i], height[j])) * (j - i)

            if area > returnVal:
                returnVal = area

            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

        return returnVal