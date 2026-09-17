# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')

        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            
            highest = max((node.val + left), (node.val + right), node.val)
            
            # print(left, right, node.val, highest)
            maxSum = max(highest, maxSum, (node.val + left + right))
            return highest

        dfs(root)
        return maxSum