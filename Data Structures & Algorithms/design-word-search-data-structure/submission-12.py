class Trie:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self): 
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        
        cur.word = True
                 

    def search(self, word: str) -> bool:

        def dfs(index, w):
            cur = w
            for i in range(index,len(word)):
                char = word[i]
                if char == ".":
                    for child in cur.children.values():
                        if dfs(i + 1,child):
                            return True
                    return False
                else:
                    if char not in cur.children:
                        return False
                    else:
                        cur = cur.children[char]

            return cur.word
                                  
        return dfs(0,self.root)
                    
                
