"""
Reasoning: recall how XOR works:
a ^ 0 = a
a ^ a = 0
a ^ b ^ a = a ^ a ^ b = (a ^ a) ^ b = 0 ^ b = b
a ^ b ^ b ^ a ^ c = (a ^ a) ^ (b ^ b) ^ c = 0 ^ 0 ^ c

With this in mind, we can check for the single element without
Extra space and in one pass
"""


def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
