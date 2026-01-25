def composeRanges(nums):
    ranges = []
    if not nums:
        return ranges
    if len(nums) == 0:
        return ranges
    if len(nums) == 1:
        return [str(nums[0])]

    firstInRange = nums[0]
    prevElement = nums[0]

    for i in range(1, len(nums)):
        if nums[i] == prevElement + 1:
            if i == len(nums) - 1:
                ranges.append(str(firstInRange) + "->" + str(nums[i]))
        else:
            if firstInRange == prevElement:
                ranges.append(str(firstInRange))
            else:
                ranges.append(str(firstInRange) + "->" + str(prevElement))

            if i == len(nums) - 1:
                ranges.append(str(nums[i]))

            firstInRange = nums[i]

        prevElement = nums[i]
    return ranges
