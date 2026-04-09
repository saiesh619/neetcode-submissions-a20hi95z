# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or root.val == p.val or root.val is q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)        
        right = self.lowestCommonAncestor(root.right,p,q)

        if left is None :
            return right
        if right is None:
            return left
        
        return root




