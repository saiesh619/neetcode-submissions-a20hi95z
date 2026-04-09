class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self,n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self,x,y):
        xp,yp = self.find(x), self.find(y)

        if self.parent[yp] == self.parent[xp]:
            return False

        if self.rank[xp] > self.rank[yp]:
            self.parent[yp] = xp

        elif self.rank[xp] < self.rank[yp]:
            self.parent[xp] = yp
        else:
            self.parent[yp] = xp
            self.rank[xp] += 1
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n+1)
        ans = []
        for u,v in edges:
            if not dsu.union(u,v):
                ans.append(u)
                ans.append(v)
        return ans
