def houseRobber(nums):
    if not nums or len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])

    solutionMatrix = [0] * len(nums)
    solutionMatrix[0] = nums[0]
    solutionMatrix[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        solutionMatrix[i] = max(solutionMatrix[i - 2] + nums[i], solutionMatrix[i - 1])

    return solutionMatrix[len(nums) - 1]
