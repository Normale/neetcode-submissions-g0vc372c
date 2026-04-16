# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pointers = list(lists)
        
        dummy = ListNode(0)
        tail = dummy
        while any(item is not None for item in pointers):
            # find smallest one among pointed values
            current_values = [(i, p.val) for i, p in enumerate(pointers) if p is not None]
            min_i, min_val = min(current_values, key=lambda x: x[1])
            # link smallest one to tail, move tail, move pointer for the linked one
            tail.next = pointers[min_i]
            tail = tail.next
            pointers[min_i] = pointers[min_i].next

        return dummy.next