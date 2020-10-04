def findMin(nums):
    if not nums or len(nums) == 0:
        return -1
    if len(nums) == 1:
        return nums[0]
        
    leftVal = 0
    rightVal = len(nums) - 1
    while (leftVal < rightVal):
        midpoint = (leftVal + rightVal) // 2
        if midpoint > 0 and nums[midpoint-1] > nums[midpoint]:
            return nums[midpoint]
        elif nums[leftVal] <= nums[midpoint] and nums[midpoint] > nums[rightVal]:
            leftVal = midpoint + 1
        else:
            rightVal = midpoint - 1
            
    return nums[leftVal]