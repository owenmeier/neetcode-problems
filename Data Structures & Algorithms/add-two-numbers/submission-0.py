# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def rec(node):
            if not node.next:
                return node.val
            return node.val + (10 * rec(node.next))

        total = rec(l1) + rec(l2)

        new = ListNode(total % 10)
        res = new
        total //= 10

        while total > 0:
            print(total)
            new.next = ListNode(total % 10)
            new = new.next
            total //= 10

        return res
            