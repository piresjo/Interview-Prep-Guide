import heapq

def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    dummy = ListNode(0)
    current = dummy
        
    heap = []
    for sorted_list in lists:
        if sorted_list:
            curr = sorted_list
            while curr:
                heapq.heappush(heap, curr.val)
                curr = curr.next
                
    while heap:
        smallest = heapq.heappop(heap)
        current.next = ListNode(smallest)
        current = current.next
                
    return dummy.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next