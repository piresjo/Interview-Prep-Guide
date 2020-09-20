def hasPathWithGivenSum(t, s):
    if t is None:
        return False

    s -= t.value
    if t.left is None and t.right is None:
        return s == 0

    return hasPathWithGivenSum(t.left, s) or hasPathWithGivenSum(t.right, s)

class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None