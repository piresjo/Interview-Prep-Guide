from typing import List


def preorderIterative(root) -> List[int]:
    res = []
    if not root:
        return res
    stack = []

    stack.append(root)

    while len(stack) > 0:
        node = stack.pop()
        res.append(node.val)
        if node.children is not None:
            reverseList = node.children[::-1]
            for child in reverseList:
                stack.append(child)

    return res
