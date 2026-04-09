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
                ch = word[i]
                if ch == ".":
                    for child in cur.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if ch not in cur.children:
                        return False
                    else:
                        cur = cur.children[ch]
            
            return cur.word

                                  
        return dfs(0,self.root)
                    
                
