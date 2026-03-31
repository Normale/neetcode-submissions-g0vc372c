# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow, fast = head, head

        prev_mid = None
        while fast and fast.next:
            fast = fast.next.next
            prev_mid = slow
            slow = slow.next
        prev_mid.next = None
        # after this is done, we have slow at HALF, fast at the end
        # 1. reorder the second half:

        prev = None
        while slow is not None:
            next_placeholder = slow.next
            slow.next = prev

            prev = slow
            slow = next_placeholder
        
        # merge reversed second half with a first half
        # for [0, 1, 2, 3, 4, 5, 6]
        # head 0 -> 1 -> 2 
        # slow = 6-> 5 -> 4 -> 3
        
        first, second = head, prev
        while first and  second:
            t1 = first.next
            t2 = second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2

