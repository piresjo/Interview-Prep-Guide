''' General Idea:
    Given the description of the problem, we have to do a BFS, keeping track of the size of each row
    The reason for this is so that once we reach the end of a row, we can calculate the average value of 
    each row.
'''

def averageOfLevels(root):
    if root is None:
        return []
    visibleQueue = []
    averageList = []
    visibleQueue.append(root)
        
    while len(visibleQueue) > 0:
        sizeVal = len(visibleQueue)
        rowVals = []
        for i in range(0, sizeVal):
            temp = visibleQueue.pop(0)
            rowVals.append(temp.val)
            if i == sizeVal - 1:
                averageList.append(sum(rowVals)/len(rowVals))
            if temp.left:
                visibleQueue.append(temp.left)
            if temp.right:
                visibleQueue.append(temp.right)
                    
    return averageList

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right