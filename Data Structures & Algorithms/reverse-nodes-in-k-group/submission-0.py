# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0

        dummy = ListNode(0, head)
        node = head
        groupPrev = dummy
        while node:
            temp = node
            while count < k:
                if temp:
                    count += 1
                    temp = temp.next
                else:
                    return dummy.next
            
            groupHead = node
            previous = temp

            while count > 0:
                # print(count, node.val)
                nextNode = node.next
                node.next = previous
                previous = node
                node = nextNode
                count -= 1

            groupPrev.next = previous
            groupPrev = groupHead
            

        return dummy.next