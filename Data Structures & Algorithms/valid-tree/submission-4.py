class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        if n - 1 != len(edges):
            return False
        
        def dfs(node,par):
            if node in visit:
                return False
            
            visit.add(node)
            for n in adj[node]:
                if par == n:
                    continue
                if not dfs(n,node):
                    return False
            return True

        print("visit", visit)
        return dfs(0,-1) and len(visit) == n