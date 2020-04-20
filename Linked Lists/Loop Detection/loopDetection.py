def whereIsLoop(head):
    pointer1 = head
    pointer2 = head

    while (True):
        if pointer2.next is None:
            return None
        if pointer2.next.next is None:
            return None
        if pointer1 == pointer2:
            return pointer1
        pointer1 = pointer1.next
        pointer2 = pointer2.next.next
