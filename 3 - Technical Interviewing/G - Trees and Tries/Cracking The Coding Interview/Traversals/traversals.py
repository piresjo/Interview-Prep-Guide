def levelOrder(root):
    if root is None:
        return None
    queue = []
    queue.append(root)
    returnString = ""
    while len(queue) != 0:
        nodeVal = queue.pop(0)
        returnString += str(nodeVal.data) + " "
        if nodeVal.left is not None:
            queue.append(nodeVal.left)
        if nodeVal.right is not None:
            queue.append(nodeVal.right)
    returnString = returnString.strip()
    return returnString


def inOrder(root):
    if root is None:
        return ""
    if root.left is None and root.right is not None:
        return str(root.data) + " " + inOrder(root.right)
    if root.right is None and root.left is not None:
        return inOrder(root.left) + " " + str(root.data)
    if root.right is None and root.left is None:
        return str(root.data)
    return inOrder(root.left) + " " + str(root.data) + " " + inOrder(root.right)


def preOrder(root):
    if root is None:
        return ""
    if root.left is None and root.right is not None:
        return inOrder(root.right) + " " + str(root.data)
    if root.right is None and root.left is not None:
        return inOrder(root.left) + " " + str(root.data)
    if root.right is None and root.left is None:
        return str(root.data)
    return inOrder(root.left) + " " + inOrder(root.right) + " " + str(root.data)


def postOrder(root):
    if root is None:
        return ""
    if root.left is None and root.right is not None:
        return str(root.data) + " " + inOrder(root.right)
    if root.right is None and root.left is not None:
        return str(root.data) + inOrder(root.left)
    if root.right is None and root.left is None:
        return str(root.data)
    return str(root.data) + " " + inOrder(root.left) + " " + inOrder(root.right)


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
