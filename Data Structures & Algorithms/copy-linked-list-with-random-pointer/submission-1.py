"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        pointers = {}

        node = head
        new = Node(head.val)
        res = new
        index = 0

        while node.next:
            new.val = node.val
            temp = Node(node.next.val)
            new.next = temp
            pointers[node] = new

            node = node.next
            new = new.next
            index += 1
        pointers[node] = new

        new = res
        node = head

        while new:
            if not node.random:
                new.random = None
            else:
                new.random = pointers[node.random]
            new = new.next
            node = node.next

        return res


