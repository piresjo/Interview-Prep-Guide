def findMiddle(list):
    if list is None or list.next is None or list.next.next is None:
        return list

    slow = list
    fast = list

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next


    return slow

class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None