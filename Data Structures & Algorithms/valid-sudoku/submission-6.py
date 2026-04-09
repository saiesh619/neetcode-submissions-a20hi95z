class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        r,c = len(board), len(board[0])

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue                
                if board[i][j] in col[j] or board[i][j] in rows[i] or board[i][j] in box[(i//3, j//3)]:
                    return False

                col[j].add(board[i][j])
                rows[i].add(board[i][j])
                box[(i//3, j//3)].add(board[i][j])
        
        return True

                
                