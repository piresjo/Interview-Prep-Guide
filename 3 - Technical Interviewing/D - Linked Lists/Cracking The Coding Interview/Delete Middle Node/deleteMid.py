# TODO - Add Method To Automatically Find The Middle Node, Then Delete, As A Side Exercise


def deleteMid(n):
    if n is None or n.next is None:
        return False

    next = n.next
    returnVal = n.data
    n.data = next.data
    n.next = next.next

    return returnVal


class LinkedList:
    def __init__(self, data, next):
        self.data = data
        self.next = next
