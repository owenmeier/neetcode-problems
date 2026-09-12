# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2:
            return list1

        one = list1
        two = list2
        head = ListNode()
        if one.val < two.val:
            head = one
            one = one.next
        else:
            head = two
            two = two.next
        
        temp = head
        

        while one and two:
            print(one.val, two.val)
            if one.val < two.val:
                temp.next = one
                one = one.next
            else:
                temp.next = two
                two = two.next
            temp = temp.next
        if one:
            temp.next = one
        else:
            temp.next = two
        return head
            

