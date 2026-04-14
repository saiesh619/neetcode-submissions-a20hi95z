class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = deque()
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for src, dest in prerequisites:
            indegree[dest] += 1
            adj[src].append(dest) 

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1            
            for n in adj[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)

        return True if finish == numCourses else False