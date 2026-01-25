def minTree(values):
    if values is None:
        return None
    if len(values) == 0:
        return None
    return minTreeMain(values, 0, len(values) - 1)


def minTreeMain(values, start, end):
    if start > end:
        return None
    midVal = start + end // 2
    n = BSTNode(values[midVal])
    n.left = minTreeMain(values, start, midVal - 1)
    n.right = minTreeMain(values, midVal + 1, len(values) - 1)

    return n


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
