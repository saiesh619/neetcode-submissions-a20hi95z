class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visit = set()
        cycle = set()
        for u,v in prerequisites:
            adj[u].append(v)
        
        def dfs(course):
            if course in cycle:
                return False
            
            if course in visit:
                return True
            
            cycle.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            
            cycle.remove(course)
            visit.add(course)
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
