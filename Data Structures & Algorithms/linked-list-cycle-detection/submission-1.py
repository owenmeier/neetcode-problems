# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        if not head:
            return False
        node = head

        while node.next:
            if node.val in seen:
                return True
            seen.add(node.val)
            node = node.next
        return False