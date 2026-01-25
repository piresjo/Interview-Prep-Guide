"""
General Idea: Utilize a sliding window, multiplying and dividing to
ensure the less than k parameter (and if we divide, we update the left
value).

For each value of right, the number of intervals with subarray product
less than k is 'right - left + 1'
"""


def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0

    left = 0
    right = 0
    result = 0
    product = 1

    while right < len(nums):
        product *= nums[right]
        while product >= k:
            product /= nums[left]
            left += 1
        result += right - left + 1
        right += 1
    return result
