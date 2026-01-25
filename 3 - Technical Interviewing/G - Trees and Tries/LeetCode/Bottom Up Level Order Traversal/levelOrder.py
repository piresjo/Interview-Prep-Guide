def levelOrderBottom(root):
    if root is None:
        return []
    queue = []
    returnList = []
    queue.append(root)

    while len(queue) > 0:
        sizeVal = len(queue)
        rowVals = []
        for i in range(0, sizeVal):
            temp = queue.pop(0)
            rowVals.append(temp.val)
            if i == sizeVal - 1:
                returnList.insert(0, rowVals)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

    return returnList


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
