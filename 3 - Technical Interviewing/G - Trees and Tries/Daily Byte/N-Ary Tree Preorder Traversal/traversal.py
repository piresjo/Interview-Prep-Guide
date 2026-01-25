from typing import List


def preorder(root: "Node") -> List[int]:
    res = []
    if not root:
        return res
    preorderHelper(root, res)
    return res


def preorderHelper(root: "Node", res: List[int]) -> List[int]:
    if not root:
        return
    res.append(root.val)
    if root.children:
        for child in root.children:
            preorderHelper(child, res)


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
