def convert(head):
    inOrderList = inOrder(head)
    return generateLinkedList(inOrderList)


def inOrder(root):
    if root is None:
        return []
    if root.left is None and root.right is not None:
        return [root.data] + inOrder(root.right)
    if root.right is None and root.left is not None:
        return inOrder(root.left) + [root.data]
    if root.right is None and root.left is None:
        return [root.data]
    return inOrder(root.left) + [root.data] + inOrder(root.right)


def generateLinkedList(list):
    if list is None or len(list) == 0:
        return None
    if len(list) == 1:
        return LinkedList(list[0])

    head = LinkedList(list[0])
    pointerA = head

    for i in range(1, len(list)):
        pointerA.next = LinkedList(list[i])
        pointerA = pointerA.next

    return head


class LinkedList:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
