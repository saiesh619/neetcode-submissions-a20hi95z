class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)

        for course,preq in prerequisites:
            preMap[course].append(preq)

        visit,cycle = set(), set()
        output = []
        def dfs(course):
            if course in visit:
                return True
            if course in cycle:
                return False
            cycle.add(course)
            for preq in preMap[course]:
                if not dfs(preq):
                    return False
            visit.add(course)
            cycle.remove(course)
            output.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return output