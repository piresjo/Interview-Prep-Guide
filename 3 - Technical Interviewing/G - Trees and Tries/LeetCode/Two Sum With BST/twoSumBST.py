def findTarget(root, k):
    if root is None:
        return False

    setVal = set()

    return find(root, k, setVal)


def find(root, k, setVal):
    if root is None:
        return False
    if k - root.val in setVal:
        return True
    setVal.add(root.val)
    return find(root.left, k, setVal) or find(root.right, k, setVal)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
