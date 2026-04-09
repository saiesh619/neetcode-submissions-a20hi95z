# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        self.dfs(root)
        return self.res
    def dfs(self,root):
        if root is None:
            return 0
        left =  max(self.dfs(root.left),0)
        right = max(self.dfs(root.right),0)
        self.res = max(self.res,left + right + root.val)     
        return root.val + max(left,right)