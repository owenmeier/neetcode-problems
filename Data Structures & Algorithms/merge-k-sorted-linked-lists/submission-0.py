# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # [0 : n/2][n/2+1 : n]
        # [...][...][...][...]
        if not lists or len(lists) == 0:
            return None
        
        def recurse(array):
            if len(array) <= 2:
                return merge(array)
            left = recurse(array[0:len(array) // 2])
            right = recurse(array[len(array) // 2:len(array)])

            return merge([left, right])

        def merge(array):
            if len(array) == 1:
                return array[0]
            
            first = array[0]
            second = array[1]
            head = ListNode()
            tail = head
            if not first and not second:
                return None
            if not first:
                return second
            if not second:
                return first

            while first and second:
                if first.val < second.val:
                    tail.next = first
                    first = first.next
                else:
                    tail.next = second
                    second = second.next
                tail = tail.next
            
            if first:
                tail.next = first
            elif second:
                tail.next = second

            return head.next

        return recurse(lists)