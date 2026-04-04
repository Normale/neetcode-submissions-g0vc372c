# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = l1, l2
        head_result = ListNode(0)
        old_head_result = head_result
        carry_on = False
        while head1 or head2:
            left = head1.val if head1 else 0
            right = head2.val if head2 else 0

            l_plus_r = left + right
            if carry_on:
                l_plus_r += 1
                carry_on = False
            if l_plus_r >= 10:
                l_plus_r = l_plus_r - 10
                carry_on = True
            curr_result = ListNode(l_plus_r)
            head_result.next = curr_result
            head_result = curr_result

            head1 = head1.next
            head2 = head2.next
        return old_head_result.next


