def findLongestSubarrayBySum(s, arr):
    left = 0
    right = 0
    returnVal = [-1]
    sumVal = 0

    while right < len(arr):
        sumVal += arr[right]
        while sumVal > s and left < right:
            sumVal -= arr[left]
            left += 1
        if sumVal == s and (
            returnVal == [-1] or returnVal[1] - returnVal[0] < right - left
        ):
            returnVal = [left + 1, right + 1]
        right += 1
    return returnVal
