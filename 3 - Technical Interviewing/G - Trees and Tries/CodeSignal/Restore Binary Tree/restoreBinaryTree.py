def restoreBinaryTree(inorder, preorder):
    if len(preorder) == 0:
        return None
    if len(preorder) == 1:
        return Tree(preorder[0])

    rootVal = Tree(preorder[0])
    dividerVal = inorder.index(preorder[0])
    leftInOrder = inorder[0:dividerVal]
    rightInOrder = inorder[dividerVal + 1 :]

    leftPreOrder = preorder[1 : dividerVal + 1]
    rightPreOrder = preorder[dividerVal + 1 :]

    rootVal.left = restoreBinaryTree(leftInOrder, leftPreOrder)
    rootVal.right = restoreBinaryTree(rightInOrder, rightPreOrder)

    return rootVal


class Tree:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
