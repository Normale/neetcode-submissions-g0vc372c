# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2 
        dummy = ListNode(0)
        tail = dummy
        while curr2 is not None and curr1 is not None:
                if curr1.val < curr2.val:        
                        tail.next = curr1
                        curr1 = curr1.next
                        tail = tail.next
                else:
                        tail.next = curr2
                        curr2 = curr2.next
                        tail = tail.next
        tail.next = curr2 if curr1 is None else curr1
        return dummy.next
                