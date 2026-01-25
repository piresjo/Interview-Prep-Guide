"""General Idea:
To generate the product without the self, you are simply getting the products of the product of
elements to the right and left of the element.

So, we need to calculate the left and right products iteratively (should be in linear time),
then multiply the left and right products together.
"""


def productExceptSelf(nums):
    lenVal = len(nums)
    lefts = [0] * lenVal
    rights = [0] * lenVal
    lefts[0] = 1
    rights[lenVal - 1] = 1

    for i in range(1, lenVal):
        lefts[i] = nums[i - 1] * lefts[i - 1]
    for i in range(lenVal - 2, -1, -1):
        rights[i] = nums[i + 1] * rights[i + 1]

    output = []
    for i in range(0, len(lefts)):
        output.append(lefts[i] * rights[i])
    return output
