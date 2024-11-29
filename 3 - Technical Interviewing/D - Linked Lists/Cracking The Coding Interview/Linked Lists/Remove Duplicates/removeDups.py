'''
    General Idea: We keep a set to determine if we've seen an element with
    that value before. If so, we modify the pointers so that it's not in
    the linked list anymore.
'''

def deleteDups(node):
    if not node:
        return node
    head = node
    setVal = set()
    prev = None
    while node:
        if node.data in setVal:
            # We don't encounter this in the first element, so NPE aren't
            # an issue here
            prev.next = None
        else:
            setVal.add(node.data)
            prev = node
        node = node.next
    return head


class LinkedList:
  def __init__(self, data, next):
    self.data = data
    self.next = next