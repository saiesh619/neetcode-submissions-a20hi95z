class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visit = set()
        for course,preq in prerequisites:
            adj[course].append(preq)

        def dfs(course):
            print("DFS CALL",course)
            if course in visit:
                return False

            if adj[course] == []:
                return True

            visit.add(course)
            preq = adj[course]
            print(preq)
            print(course)
            print(visit)
            for courses in preq:
                if not dfs(courses):
                    return False
            visit.remove(course)
            adj[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True
