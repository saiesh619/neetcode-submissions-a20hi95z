class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, col = len(grid),len(grid[0])
        fresh = 0
        for i in range(rows):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append([i,j])
                if grid[i][j] == 1:
                    fresh += 1

        minute = 0
        directions =[[0,1],[1,0],[-1,0],[0,-1]]

        while q and fresh > 0:
            qL = len(q)
            for i in range(qL):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr >= 0 and nc >= 0 and nr < rows and nc < col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append([nr,nc])
                        fresh -= 1
            minute += 1
        
        if fresh == 0:
            return minute
        else:
            return -1