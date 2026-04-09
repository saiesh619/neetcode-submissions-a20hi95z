class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        cycle = set()
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[u].append(v)
        def dfs(course):
            if course in cycle:
                return False
            
            if adj[course] == []:
                return True
            
            cycle.add(course)

            for preq in adj[course]:
                if not dfs(preq):
                    return False
            cycle.remove(course)
            adj[course] = []
            return True


        for c in range(numCourses):
            if not dfs(c):
                return False

        return True 
            

