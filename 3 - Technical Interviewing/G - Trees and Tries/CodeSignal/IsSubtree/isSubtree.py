def isSubtree(t1, t2):
    if not t2:
        return True
    return subtree(t1, t2)


def subtree(t1, t2):
    if not t1:
        return False
    if t1.value == t2.value and matchTree(t1, t2):
        return True

    return subtree(t1.left, t2) or subtree(t1.right, t2)


def matchTree(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.value != t2.value:
        return False

    return matchTree(t1.left, t2.left) and matchTree(t1.right, t2.right)


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
