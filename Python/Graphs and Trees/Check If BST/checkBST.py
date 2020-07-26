def isBST(root):
	return isBSTMain(root, None, None)

def isBSTMain(root, minVal, maxVal):
	if root is None:
		return True

	if (minVal is not None and minVal >= root.data) or (maxVal is not None and maxVal < root.data):
		return False

	if isBSTMain(root.left, minVal, root.data) is False or isBSTMain(root.right, root.data, maxVal) is False:
		return False

	return True

class BSTNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None