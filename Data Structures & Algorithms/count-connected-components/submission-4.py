class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self,node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    
    def union(self,u,v):
        up, vp = self.find(u), self.find(v)
        if up == vp:
            return False
        if self.rank[up] > self.rank[vp]:
            self.parent[vp] = up
        elif self.rank[vp] > self.rank[up]:
            self.parent[up] = vp
        else:
            self.parent[up] = vp
            self.rank[vp] += 1
        return True    
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n
        dsu = DSU(n)
        for u,v in edges:
            if dsu.union(u,v):
                res -= 1
        return res