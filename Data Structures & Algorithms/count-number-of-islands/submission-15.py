class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, col = len(grid), len(grid[0])
        s = 0
        visit = set()


        def dfs(r,c):
            if r < rows and c < col and r >= 0 and c >= 0 and grid[r][c] != "0" and (r,c) not in visit:
                visit.add((r,c))
            
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)

        
        for i in range(rows):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in visit:
                    dfs(i,j)
                    s += 1
        
        return s