def intersection(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)

    returnList = []
    for x in nums1:
        if x in nums2:
            returnList.append(x)
    return returnList


def intersectionAlt(nums1, nums2):
    numsDict1 = {}
    numsDict2 = {}

    for num in nums1:
        if num not in numsDict1:
            numsDict1[num] = 1
        else:
            numsDict1[num] += 1

    for num in nums2:
        if num not in numsDict2:
            numsDict2[num] = 1
        else:
            numsDict2[num] += 1

    res = []

    for key, value in numsDict1.items():
        if key in numsDict2:
            res.append(key)

    return res
