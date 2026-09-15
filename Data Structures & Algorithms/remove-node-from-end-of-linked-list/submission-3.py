# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        node = head
        left = head

        for i in range(n):
            node = node.next

        if not node:
            return head.next
        
        while node.next:
            
            node = node.next
            left = left.next

        left.next = left.next.next

        return head
