class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0 
        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 :
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))
        
        directions =[[0,1],[1,0] ,[0, -1], [-1,0]]
        while fresh > 0 and q:
            qL = len(q)
            for i in range(qL):
                r,c = q.popleft()

                for dr,dc in directions:
                    row,col = r + dr, c + dc
                    if row < len(grid) and col < len(grid[0]) and grid[row][col] == 1 and row >= 0 and col >=0:
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1 
        