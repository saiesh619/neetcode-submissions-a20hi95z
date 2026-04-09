class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1] * n 

    def find(self,n):
        if n != self.parent[n]:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    
    def union(self,q,r):
        qp, rp = self.find(q), self.find(r)

        if qp == rp:
            return False
        
        if self.rank[qp] > self.rank[rp]:
            self.parent[rp] = qp
        elif self.rank[qp] < self.rank[rp]:
            self.parent[qp] = rp
        else:
            self.parent[qp] = rp 
            self.rank[rp] += 1

        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n+1)
        
        for u,v in edges:
            if not dsu.union(u,v):
                return [u,v]
        return []
