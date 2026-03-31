# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # after this is done, we have slow at HALF, fast at the end
        # 1. reorder the second half:

        prev = None
        while slow is not None:
            next_placeholder = slow.next
            slow.next = prev

            prev = slow
            slow = next_placeholder
        
        # merge reversed second half with a first half
        i = 0
        dummy = ListNode(0)
        old_dummy = dummy
        # for [0, 1, 2, 3, 4, 5, 6]
        # head 0 -> 1 -> 2 
        # slow = 3-> 4 -> 5 -> 6
        while head and slow:
            if i % 2:
                dummy.next = head
                head = head.next
            else:
                dummy.next = slow
                slow = slow.next
            dummy = dummy.next
            i += 1
        return dummy.next





