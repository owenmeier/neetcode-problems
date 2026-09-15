# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, largest):
            if not node:
                return 0
            if node.val >= largest:
                return 1 + dfs(node.left, max(node.val, largest)) + dfs(node.right, max(node.val, largest))
            return dfs(node.left, max(node.val, largest)) + dfs(node.right, max(node.val, largest))

        return dfs(root, root.val)