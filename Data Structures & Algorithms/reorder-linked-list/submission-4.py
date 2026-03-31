class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def print_list(node, label):
            vals = []
            while node:
                vals.append(str(node.val))
                node = node.next
            print(f"{label}: " + " -> ".join(vals))

        print_list(head, "initial")

        slow, fast = head, head

        # find middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        print(f"middle at: {slow.val if slow else None}")

        # reverse second half
        prev = None
        while slow is not None:
            next_placeholder = slow.next
            slow.next = prev

            print(f"reversing node {slow.val}, next set to {prev.val if prev else None}")

            prev = slow
            slow = next_placeholder

        # after reverse, prev is head of reversed half
        slow = prev
        print_list(slow, "reversed second half")
        print_list(head, "first half before merge")

        # merge
        i = 0
        dummy = ListNode(0)
        old_dummy = dummy

        while head and slow:
            if i % 2:
                print(f"take from first half: {head.val}")
                dummy.next = head
                head = head.next
            else:
                print(f"take from second half: {slow.val}")
                dummy.next = slow
                slow = slow.next

            dummy = dummy.next
            i += 1
            print_list(old_dummy.next, "merged so far")

        print_list(old_dummy.next, "final merged")
        return 