def deleteMid(n):
    if n is None or n.next is None:
        return False
    
    next = n.next
    n.data = next.data
    n.next = next.next

    return True
