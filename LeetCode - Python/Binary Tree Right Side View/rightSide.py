'''
    Solution Summary:
    Key words here are 'top to bottom'. This is likely a BFS solution
    We need a modified BFS. We need a way to determine the rightmost element in a row
    Given BFS, it would be the last element in the row
    Time and Space - O(n)
'''

def rightSideView(root):
    if root is None:
        return []
    visibleQueue = []
    visibleList = []
    visibleQueue.append(root)
        
    while len(visibleQueue) > 0:
        sizeVal = len(visibleQueue)
        for i in range(0, sizeVal):
            temp = visibleQueue.pop(0)
            if i == sizeVal - 1:
                visibleList.append(temp.val)
            if temp.left:
                visibleQueue.append(temp.left)
            if temp.right:
                visibleQueue.append(temp.right)
                
        
    return visibleList

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right