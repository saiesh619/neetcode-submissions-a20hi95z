class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        ans = 0
        rows, col = len(grid), len(grid[0])

        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= col or grid[r][c] == "0" or (r,c) in visit:
                return   

            visit.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for i in range(rows):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in visit:                    
                    dfs(i,j)
                    print(visit)
                    print(i,j)
                    ans += 1
        return ans