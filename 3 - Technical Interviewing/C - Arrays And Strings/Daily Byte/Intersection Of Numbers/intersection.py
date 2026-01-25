def intersection(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)

    returnList = []
    for x in nums1:
        if x in nums2:
            returnList.append(x)
    return returnList
