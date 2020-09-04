'''
    Solution Summary:
    This solution allows us to iterate through the string once
    Set a dict. We're looking for compliments to other numbers to get the target
'''

def twoSum(nums, target):
    if not nums or not target:
        return []
    complimentDict = {}
    for i in range(0, len(nums)):
        if target - nums[i] in complimentDict:
            return [complimentDict[target - nums[i]], i]
        else:
            complimentDict[nums[i]] = i
    return []