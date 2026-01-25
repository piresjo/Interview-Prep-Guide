def find(head, val):
    if head is None:
        return None

    if val is None:
        return None

    if head.data == val:
        return head

    if val > head.data:
        return find(head.right, val)
    else:
        return find(head.left, val)


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
