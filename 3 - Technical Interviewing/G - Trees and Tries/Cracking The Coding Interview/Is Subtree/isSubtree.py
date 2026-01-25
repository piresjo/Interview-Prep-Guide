def isSubtree(node1, node2):
    if node1 is None or node2 is None:
        return False
    sb1 = ""
    orderedString1 = orderedString(node1, sb1)
    orderedString2 = orderedString(node2, "")
    return orderedString2 in orderedString1


def orderedString(root, stringVal):
    if root is None:
        stringVal += "X"
        return stringVal

    stringVal += str(root.data)
    stringVal += " "

    return orderedString(root.left, stringVal)
    return orderedString(root.right, stringVal)


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
