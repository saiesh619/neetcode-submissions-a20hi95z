class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        visit = set()
        q = deque()
        fresh = [1]
        fresh[0] = 0
        def rotFruit(r,c):
            if (r,c) in visit or r == rows or c == cols or r < 0 or c < 0 or grid[r][c] == 0:
                return False
            q.append([r,c])
            visit.add((r,c))
            grid[r][c] = 2
            fresh[0] = fresh[0] - 1            
            return True
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append([i,j])
                    visit.add((i,j))
                if grid[i][j] == 1:
                    fresh[0] += 1
        t = 0
        while len(q):
            qL = len(q)              
            changed = False
            for i in range(qL):                                           
                r,c = q.popleft()
                
                changed |= rotFruit(r + 1 ,c)
                changed |= rotFruit(r - 1 ,c)
                changed |= rotFruit(r ,c - 1)
                changed |= rotFruit(r ,c + 1)
            if changed:
                t += 1

        if fresh[0] <= 0:
            print(fresh[0])
            return t 
        return -1 