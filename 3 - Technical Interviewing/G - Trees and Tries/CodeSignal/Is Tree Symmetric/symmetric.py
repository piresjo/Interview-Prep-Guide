def isTreeSymmetric(t):
    if not t:
        return True
    return symmetric(t.left, t.right)


def symmetric(l, r):
    if not l and not r:
        return True
    if not l or not r:
        return False

    if l.value == r.value:
        return symmetric(l.right, r.left) and symmetric(l.left, r.right)

    return False


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
