class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visit = set()
        for u, v in edges:
            adj[v].append(u)
            adj[u].append(v)
        
        def dfs(node,par):
            if node in visit:
                return False
            
            visit.add(node)

            for n in adj[node]:
                if n == par:
                    continue
                if not dfs(n,node):
                    return False
            return True
        
        return dfs(0,-1) and len(visit) == n 
