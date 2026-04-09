class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict

        adj = defaultdict(list)
        visit = set()
        output = []

        # Build graph: prereq -> course
        for course, preq in prerequisites:
            adj[preq].append(course)

        def dfs(course):
            if course in visit:
                return False
            if adj[course] == []:
                output.append(course)
                return True

            visit.add(course)
            for nxt in adj[course]:
                if not dfs(nxt):
                    return False
            visit.remove(course)
            output.append(course)
            adj[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return output[::-1]
