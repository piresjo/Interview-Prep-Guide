def nextGreaterElement(nums1, nums2):
    nextGreatest = {}
    stack = []
        
    for num in nums2:
        while(len(stack) != 0 and stack[-1] < num):
            nextGreatest[stack.pop()] = num
            
        stack.append(num)
        
    returnList = []
        
    for num in nums1:
        if num not in nextGreatest:
            returnList.append(-1)
        else:
            returnList.append(nextGreatest[num])
    return returnList