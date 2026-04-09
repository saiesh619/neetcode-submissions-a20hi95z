# Definition for a binary tree node.

# class TreeNode:

# def **init**(self, val=0, left=None, right=None):

# self.val = val

# self.left = left

# self.right = right

class Solution:
    rank = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.rank = k
        self.dfs(root)
        return self.ans

    
    def dfs(self,root):
        if root is None:
            return
        self.dfs(root.left)
        self.rank = self.rank - 1
        if self.rank == 0:
            self.ans = root.val
        self.dfs(root.right)
        

