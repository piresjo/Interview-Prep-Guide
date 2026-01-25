def kthSmallestInBST(t, k):
    if not t:
        return None
    inOrderArray = []
    inOrder(t, inOrderArray)
    return inOrderArray[k - 1]


def inOrder(t, inOrderArray):
    if t is None:
        return
    elif t.left is None and t.right is not None:
        inOrderArray.append(t.value)
        inOrder(t.right, inOrderArray)
    elif t.right is None and t.left is not None:
        inOrder(t.left, inOrderArray)
        inOrderArray.append(t.value)
    elif t.right is None and t.left is None:
        inOrderArray.append(t.value)
    else:
        inOrder(t.left, inOrderArray)
        inOrderArray.append(t.value)
        inOrder(t.right, inOrderArray)


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
