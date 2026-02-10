from typing import List


def plusOne(digits: List[int]) -> List[int]:
    end = len(digits) - 1
    digits[end] += 1

    while digits[end] == 10:
        digits[end] = 0
        if (end - 1) < 0:
            digits = [1] + digits
        else:
            digits[end - 1] += 1
            end -= 1

    return digits
