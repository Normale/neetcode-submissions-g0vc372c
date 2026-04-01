# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow, fast = head, head
        if not head:
                return None
        if not head.next:
                return None

        for _ in range(n):
                fast = fast.next
        # now the fast is N steps ahead of slow
        prev = slow

        # edge case: if N = length of the list, fast is None already, and we need to remove first node
        if fast is None:
                return head.next
        while fast is not None:
                fast = fast.next
                prev = slow
                slow = slow.next
        # when the fast is at the end, slow will be n-steps from the end
        prev.next = slow.next
        return head