class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        rows, col = len(grid), len(grid[0])
        res = 0
        def dfs(r,c):
            if r >= 0 and c >= 0 and r < rows and c < col and (r,c) not in visit and grid[r][c] != 0:
                visit.add((r,c))
                return( dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1) + 1
                )
            return 0


        for i in range(rows):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in visit:
                   res = max(res,dfs(i,j))
        return res