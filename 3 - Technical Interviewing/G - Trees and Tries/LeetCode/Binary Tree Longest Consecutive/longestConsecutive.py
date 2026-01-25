"""
Solution Summary:
Since we're going through a binary tree, we can recurse through the tree.
This means we should get an auxillary recursive method.
A single node would make the maxSize 1, if the target wasn't matched (or if it's the starting node).
By having an array (which is byRef), we can just modify the maxLength with relative ease
"""


def longestConsecutive(node):
    maxVal = [0]
    largestConsecutiveAux(node, 0, 0, maxVal)
    return maxVal[0]


def largestConsecutiveAux(nodeVal, target, maxSize, maxArray):
    if nodeVal is None:
        return
    if nodeVal.val == target:
        maxSize += 1
    else:
        maxSize = 1

    maxArray[0] = max(maxArray[0], maxSize)
    largestConsecutiveAux(nodeVal.left, nodeVal.val + 1, maxSize, maxArray)
    largestConsecutiveAux(nodeVal.right, nodeVal.val + 1, maxSize, maxArray)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
