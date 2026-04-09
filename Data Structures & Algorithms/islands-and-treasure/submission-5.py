class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit = set()
        rows, col = len(grid), len(grid[0])
        q = deque()
        dist = 0

        for i in range(rows):
            for j in range(col):
                if grid[i][j] == 0 :
                    q.append([i,j])
                    visit.add((i,j))
        directions =[[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            qL = len(q)
            for i in range(qL):
                r,c = q.popleft()
                grid[r][c] = dist

                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc 
                    if nr >= 0 and nc >= 0 and nc < col and nr < rows and (nr,nc) not in visit and grid[nr][nc] != -1:
                        visit.add((nr,nc))
                        q.append([nr,nc])
                    


            dist += 1