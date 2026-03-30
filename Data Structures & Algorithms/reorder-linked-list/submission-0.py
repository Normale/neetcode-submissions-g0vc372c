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

        curr = slow
        prev = None
        while curr is not None:
            next_placeholder = curr.next
            curr.next = prev

            prev = curr
            curr = next_placeholder
        
        # merge reversed second half with a first half
        i = 0
        dummy = ListNode(0)
        old_dummy = dummy
        while head and slow:
            if i % 2:
                dummy.next = head
                head = head.next
            else:
                dummy.next = slow
                slow = slow.next
            dummy = dummy.next
        return dummy.next





