# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        res = []
        q.append(root)
        if root :
            while len(q):
                length = len(q)
                level = []
                for i in range(length):
                    first = q.popleft()
                    level.append(first.val)
                    if first.left:
                        q.append(first.left)
                    if first.right:
                        q.append(first.right)                
                res.append(level[len(level) - 1])
        return res