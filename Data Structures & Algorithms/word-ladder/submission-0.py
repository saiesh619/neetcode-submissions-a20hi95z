class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        q.append((beginWord,0))
        step = 0
        visit = set()
        while q:
            qL = len(q)            
            for i in range(qL):
                word, step = q.popleft()
                if word == endWord:
                    return step + 1
                wordLength = len(word)
                for w in wordList:
                    count = 0
                    for i in range(len(w)):
                        if w[i] != word[i]:
                            count += 1
                    if count == 1 and w not in visit:
                        visit.add(w)
                        q.append((w ,step + 1))
        return 0