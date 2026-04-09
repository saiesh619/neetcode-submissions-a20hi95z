class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        col = len(grid[0])
    
        visit = set()
        count = 0
        
        
        

        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= col or (r,c) in visit or grid[r][c] == "0":
                return 
            visit.add((r,c))
            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r,c + 1)
            dfs(r ,c -1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visit:
                    count += 1
                    dfs(i,j)

        return count