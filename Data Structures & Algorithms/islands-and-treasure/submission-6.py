class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        INF = 2**31 - 1
        rows, col = len(grid), len(grid[0])
        visit = set()
        distance = 0
        for i in range(rows):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visit.add((i,j))

        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        while q :
            n = len(q)
            for i in range(n):
                r,c = q.popleft()

                for dr,dc in dir:
                    nr,nc = r + dr, c + dc

                    if nr >= 0 and nc >= 0 and nr < rows and nc < col and grid[nr][nc] == INF:
                        q.append((nr,nc))
                        visit.add((nr,nc))
                        grid[nr][nc] = distance + 1
                
            distance += 1
        
                        
        



