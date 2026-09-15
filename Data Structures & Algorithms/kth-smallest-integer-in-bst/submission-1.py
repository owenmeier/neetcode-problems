# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(node, depth):
            if not node:
                return None
            dfs(node.left, depth + 1)
            res.append(node.val)
            dfs(node.right, depth + 1)
            

        dfs(root, 0)
        # print(res)
        return res[k - 1]