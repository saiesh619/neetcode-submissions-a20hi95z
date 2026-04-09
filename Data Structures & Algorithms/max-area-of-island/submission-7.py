class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        maxCount = 0
        rows, col = len(grid), len(grid[0])
        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= col or (r,c) in visit or grid[r][c] == 0:
                return 0

            visit.add((r,c))
            count =   dfs(r + 1,c) + dfs(r - 1,c) + dfs(r ,c + 1) + dfs(r ,c - 1) + 1

            return count
            
        
        for i in range(rows):
            for j in range(col):                
                if grid[i][j] == 1 and (i,j) not in visit:
                    print("here")
                    maxCount = max(dfs(i,j), maxCount)    

        return maxCount