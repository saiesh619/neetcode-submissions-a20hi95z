class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, col = len(heights), len(heights[0])
        atlantic = set()
        pacific = set()
        def dfs(r,c,visit,h):
            if r < 0 or c < 0 or r == rows or c == col or (r,c) in visit or heights[r][c] < h:
                return
            visit.add((r,c))                             
            dfs(r + 1, c,visit,heights[r][c])
            dfs(r - 1, c,visit,heights[r][c])
            dfs(r, c + 1,visit,heights[r][c])
            dfs(r, c - 1,visit,heights[r][c])

        for i in range (rows):
            dfs(i,0,pacific,heights[i][0])
            dfs(i,col - 1,atlantic,heights[i][col -1])
        for j in range (col):
            dfs(0,j,pacific,heights[0][j])
            dfs(rows - 1,j,atlantic,heights[rows -1][j])
        res = []
        for i in range (rows):
            for j in range (col):
                if (i,j) in atlantic and (i,j) in pacific:
                    res.append([i,j])

        return res
        
