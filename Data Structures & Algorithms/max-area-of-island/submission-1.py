class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
        maxCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxCount = max(self.dfs(grid,i,j),maxCount)
        return maxCount 

    def dfs(self,grid,r,c):
        if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c] == 0:
            return 0
        
        count = 1
        grid[r][c] = 0
        return (1 + self.dfs(grid,r + 1 ,c) + self.dfs(grid,r - 1, c) + self.dfs(grid,r, c + 1) + self.dfs(grid,r, c - 1))

