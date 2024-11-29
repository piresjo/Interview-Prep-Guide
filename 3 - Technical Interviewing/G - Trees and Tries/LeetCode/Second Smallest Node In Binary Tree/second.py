def findSecondMinimumValue(root):
    uniques = set()
    traverse(root, uniques)
        
    minVal = root.val
    secondMin = float("inf")
    for value in uniques:
        if minVal < value < secondMin:
            secondMin = value
                
    return secondMin if secondMin < float("inf") else -1
        
def traverse(node, uniques):
    if node:
        uniques.add(node.val)
        traverse(node.left, uniques)
        traverse(node.right, uniques)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right