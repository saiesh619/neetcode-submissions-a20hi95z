# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    Balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root)
        return self.Balanced
    
    def dfs(self,root):
        if root is None:
            return 0

        
        left = self.dfs(root.left) + 1
        right = self.dfs(root.right) + 1
        difference = left - right
        if abs(difference) > 1:
            self.Balanced = False
        return(max(left,right))
    