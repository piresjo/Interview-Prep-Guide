'''
    General Idea - We can do BFS while keeping track of the layers
    As we go through each layer, we replace the sum of the layer. The sum of
    the deepest layer will be the last sum value we get, which we return
'''

def deepestLeavesSum(root):
    if root is None:
        return 0
    queue = []
    returnVal = 0
    queue.append(root)
        
    while len(queue) > 0:
        sizeVal = len(queue)
        sumVal = 0
        for i in range(0, sizeVal):
            temp = queue.pop(0)
            sumVal += temp.val
            if i == sizeVal - 1:
                returnVal = sumVal
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
                    
    return returnVal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right