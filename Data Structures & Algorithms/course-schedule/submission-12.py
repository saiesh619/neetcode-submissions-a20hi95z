class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        q = deque()
        adj = defaultdict(list)
        finish = 0

        for u,v in prerequisites:            
            adj[v].append(u)
            indegree[u] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            finish += 1
            for c in adj[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
        
        return True if finish == numCourses else False