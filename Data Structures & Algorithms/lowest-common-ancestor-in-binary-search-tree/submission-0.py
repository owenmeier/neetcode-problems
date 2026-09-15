# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # possible answers: [p: q] inclusive
        lower = p.val
        upper = q.val
        if p.val > q.val:
            lower = q.val
            upper = p.val
        node = root

        while True:
            if node.val == lower or node.val == upper:
                return node
            elif lower < node.val < upper:
                return node
            elif node.val > upper:
                node = node.left
            elif node.val < lower:
                node = node.right


