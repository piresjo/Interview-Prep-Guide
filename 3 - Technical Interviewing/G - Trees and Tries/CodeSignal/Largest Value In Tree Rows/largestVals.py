def largestValuesInTreeRows(t):
    if t is None:
        return []
    queue = []
    returnList = []
    queue.append(t)

    while len(queue) > 0:
        sizeVal = len(queue)
        maxVal = float("-inf")
        for i in range(0, sizeVal):
            temp = queue.pop(0)
            if temp.value > maxVal:
                maxVal = temp.value
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        returnList.append(maxVal)

    return returnList


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
