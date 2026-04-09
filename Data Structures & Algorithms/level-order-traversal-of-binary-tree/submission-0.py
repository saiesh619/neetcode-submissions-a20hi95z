# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()        
        level = []
        q.append(root)
        res = []
        if root :
            while len(q) != 0 :
                level = []
                length = len(q)            
                for i in range(length):
                    first = q.popleft()
                    level.append(first.val) 
                
                    if first.left:
                        q.append(first.left)
                    if first.right:
                        q.append(first.right)
                res.append(level)
        return res

        


