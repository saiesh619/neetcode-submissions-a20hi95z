class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        rows, col = len(grid), len(grid[0])
        ans = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= col or grid[r][c] == 0 or (r,c) in visit:
                return 0

            visit.add((r,c))

            return(
                1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r, c+1) + dfs(r, c-1)
            )

        for i in range(rows):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in visit:
                    ans = max(ans,dfs(i,j))
        
        return ans
