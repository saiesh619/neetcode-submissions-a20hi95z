class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        q = deque()
        fruits = 0
        rows = len(grid)
        col = len(grid[0])

        for i in range(rows):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fruits += 1

        directions = [[0,1], [1,0], [0,-1],[-1,0]]
        
        while q and fruits > 0:
            n = len(q)
            for i in range(n):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r + dr, c + dc
                    if nr >= 0 and nc >= 0 and nr < rows and nc < col:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            q.append((nr,nc))
                            fruits -= 1
            time += 1
        return time if fruits == 0 else  -1