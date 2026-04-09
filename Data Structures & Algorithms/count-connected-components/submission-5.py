class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self,n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self,a,b):
        ap,bp = self.find(a), self.find(b)
        if self.parent[ap] == self.parent[bp]:
            return False
        if self.rank[ap] > self.rank[bp]:
            self.parent[bp] = ap 
        elif self.rank[ap] < self.rank[bp]:
            self.parent[ap] = bp
        else:
            self.parent[ap] = bp
            self.rank[bp] += 1
        return True
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = n
        dsu = DSU(n)
        for u,v in edges:
            if dsu.union(u,v):
                ans -= 1
        return ans         