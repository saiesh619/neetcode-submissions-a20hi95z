# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root,root.val)
        return self.res

    def dfs(self,root,val):
        if root is None :
            return
        
        if root.val >= val :
            self.res += 1

        self.dfs(root.left,max(val,root.val))
        self.dfs(root.right,max(val,root.val))
