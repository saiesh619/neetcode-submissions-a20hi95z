class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        def addCell(r,c):
            if (r,c) in visit or r >= rows or c >= cols or r < 0 or c < 0 or grid[r][c] == -1:
                return 
            q.append([r,c])
            visit.add((r,c))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 :
                    q.append([i,j])
                    visit.add((i,j))
        
        dist = 0
        while q:            
            qL = len(q)
            for i in range(qL):
                r,c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1,c)
                addCell(r - 1,c)
                addCell(r,c + 1)
                addCell(r,c - 1)
            dist += 1
