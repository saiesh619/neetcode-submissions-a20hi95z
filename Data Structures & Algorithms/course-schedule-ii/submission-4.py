class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[u].append(v)
        
        visit = set()
        completed = set()
        order = []
        def dfs(course):
            if course in visit:
                return False
            
            if course in completed:
                return True

            visit.add(course)            
            for preq in adj[course]:
                if not dfs(preq):
                    return False
            completed.add(course)
            visit.remove(course)
            order.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order
            

        