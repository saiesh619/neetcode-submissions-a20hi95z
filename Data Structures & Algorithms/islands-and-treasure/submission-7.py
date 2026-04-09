class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        q = deque()
        rows = len(grid)
        col = len(grid[0])
        for i in range(rows):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        dist = 0
        while q:
            n = len(q)
            dist += 1
            for i in range(n):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r + dr, c + dc
                    if nr >= 0 and nc >= 0 and nc < col and nr < rows:
                        if grid[nr][nc] == INF:
                            grid[nr][nc] = dist
                            q.append((nr,nc))
        
