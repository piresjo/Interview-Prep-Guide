def digitTreeSum(t):
    # Given the nature of the problem, use DFS to get all the distinct sets of digits to add up
    return digitTreeAux(t, 0)


def digitTreeAux(t, sumVal):
    if not t:
        return 0

    # In a 4 level path, the top node is in the thousands place, the second is in the hundreds, and so on
    sumVal = (sumVal * 10) + t.value

    if not t.left and not t.right:
        return sumVal

    # Since we're adding all the sets of digits, we can just recurse like this
    return digitTreeAux(t.left, sumVal) + digitTreeAux(t.right, sumVal)


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
