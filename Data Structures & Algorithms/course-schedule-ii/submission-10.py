class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        q = deque()
        finish = 0
        orderOfCourses = []
        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)

        
        while q:
            course = q.popleft()
            orderOfCourses.append(course)
            finish += 1
            for c in adj[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
        return orderOfCourses if finish == numCourses else []