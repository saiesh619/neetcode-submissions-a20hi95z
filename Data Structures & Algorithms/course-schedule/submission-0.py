class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        for course,preq in prerequisites:
            preMap[course].append(preq)

        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if preMap[course] == []:
                return True
            visit.add(course)
            for preq in preMap[course]:
                if not dfs(preq):
                    return False
            visit.remove(course)
            preMap[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        

        