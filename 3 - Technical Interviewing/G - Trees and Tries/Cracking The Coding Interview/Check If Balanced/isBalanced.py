import sys


def checkHeight(root):
    if root is None:
        return -1

    leftHeight = checkHeight(root.left)
    if leftHeight == -(sys.maxsize - 1):
        return -(sys.maxsize - 1)

    rightHeight = checkHeight(root.right)
    if rightHeight == -(sys.maxsize - 1):
        return -(sys.maxsize - 1)

    diff = abs(leftHeight - rightHeight)

    if diff > 1:
        return -(sys.maxsize - 1)
    else:
        return max(leftHeight, rightHeight) + 1


def isBalanced(root):
    return checkHeight(root) != -(sys.maxsize - 1)


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
