def levelOrder(root):
    if root is None:
        return None
    queue = []
    queue.append(root)
    returnString = ""
    while len(queue) != 0:
        nodeVal = queue.pop(0)
        returnString += str(nodeVal.data) + ' '
        if nodeVal.left is not None:
            queue.append(nodeVal.left)
        if nodeVal.right is not None:
            queue.append(nodeVal.right)
    returnString = returnString.strip()
    return returnString


class BSTNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None