class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        dist = 0
        rows = len(grid)
        col = len(grid[0])
        q = deque()

        for i in range(rows):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i,j))
        

        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        while q:
            n = len(q)
            dist += 1
            for i in range(n):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr , nc = r + dr, c + dc
                    if nr >= 0 and nc >= 0 and nr < rows and nc < col:
                        if grid[nr][nc] == INF:
                            grid[nr][nc] = dist
                            q.append((nr,nc))
                        
        
        

