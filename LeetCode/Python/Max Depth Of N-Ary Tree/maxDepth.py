def maxDepth(root):
    if root is None:
        return 0
    queue = []
    depth = 0
    queue.append(root)
        
    while len(queue) > 0:
        sizeVal = len(queue)
        for i in range(0, sizeVal):
            temp = queue.pop(0)
            queue += temp.children
        depth += 1
                    
    return depth

class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children