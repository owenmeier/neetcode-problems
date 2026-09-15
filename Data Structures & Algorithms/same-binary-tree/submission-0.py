# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        left = []
        right = []

        def dfs(rootA, rootB):
            if not rootA and not rootB:
                return True
            elif not rootA:
                return False
            elif not rootB:
                return False
            elif rootA.val == rootB.val:
                return dfs(rootA.left, rootB.left) and dfs(rootA.right, rootB.right)
            else:
                return False
            
            

        return dfs(p, q)