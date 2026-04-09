class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def addWord(self, word):
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.word = True                


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        rows,col = len(board), len(board[0])
        visit,res = set(),set()
        def dfs(r,c,root,word):
            if r < 0 or c < 0 or r >= rows or c >= col or board[r][c] not in root.children or (r,c) in visit:
                return

            visit.add((r,c))
            root = root.children[board[r][c]]
            word += board[r][c]

            if root.word:
                res.add(word)

            dfs(r+1,c,root,word)
            dfs(r-1,c,root,word)
            dfs(r,c+1,root,word)
            dfs(r,c-1,root,word)

            visit.remove((r,c))

        for i in range(rows):
            for j in range(col):
                dfs(i,j,root,"")
        
        return list(res)
