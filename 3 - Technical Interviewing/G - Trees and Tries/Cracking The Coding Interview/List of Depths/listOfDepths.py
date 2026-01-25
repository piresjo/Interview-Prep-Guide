def listOfDepths(node):
    if node is None:
        return []
    visibleQueue = []
    visibleList = []
    visibleQueue.append(node)

    while len(visibleQueue) > 0:
        sizeVal = len(visibleQueue)
        levelList = []
        for i in range(0, sizeVal):
            temp = visibleQueue.pop(0)
            levelList.append(temp.val)
            if temp.left:
                visibleQueue.append(temp.left)
            if temp.right:
                visibleQueue.append(temp.right)
        visibleList.append(levelList)

    return visibleList


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
