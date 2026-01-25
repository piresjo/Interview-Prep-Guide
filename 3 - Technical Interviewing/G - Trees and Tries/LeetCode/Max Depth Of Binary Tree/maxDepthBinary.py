def maxDepth(root) -> int:
    if root is None:
        return 0
    queue = []
    depth = 0
    queue.append(root)

    while len(queue) > 0:
        sizeVal = len(queue)
        for i in range(0, sizeVal):
            temp = queue.pop(0)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        depth += 1

    return depth


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
