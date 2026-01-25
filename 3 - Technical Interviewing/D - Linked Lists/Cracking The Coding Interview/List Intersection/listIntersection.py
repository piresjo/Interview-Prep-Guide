def isIntersection(list1, list2):
    if list1 is None or list2 is None:
        return None

    tail1 = getTail(list1)
    tail2 = getTail(list2)
    len1 = getSize(list1)
    len2 = getSize(list2)

    if tail1 != tail2:
        return None

    offset = abs(len1 - len2)
    biggerList = None
    smallerList = None
    if offset == 0:
        biggerList = list1
        smallerList = list2
    else:
        biggerList = list1 if len1 > len2 else list2
        smallerList = list2 if len1 > len2 else list1
        for i in range(0, offset):
            biggerList = biggerList.next

    while biggerList is not None:
        if biggerList == smallerList:
            return biggerList
        biggerList = biggerList.next
        smallerList = smallerList.next


def getTail(listVal):
    pointer = listVal
    while pointer.next is not None:
        pointer = pointer.next
    return pointer


def getSize(listVal):
    pointer = listVal
    counter = 0
    while pointer is not None:
        counter += 1
        pointer = pointer.next
    return counter


class LinkedList:
    def __init__(self, data, next):
        self.data = data
        self.next = next
