class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        cycle = set()
        visit = set()
        output = []
        for u,v in prerequisites:
            adj[u].append(v)

        
        def dfs(course):
            if course in cycle:
                return False
            
            if course in visit:
                return True
            
            cycle.add(course)
            
            for preq in adj[course]:
                if not dfs(preq):
                    return False
            
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return output