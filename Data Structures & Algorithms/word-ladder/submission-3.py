class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        q.append((beginWord,1))
        step = 0
        wordList = set(wordList)
        while q:
            word, count = q.popleft()
            if word == endWord:
                return count
            
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        q.append([next_word,count + 1])
                        wordList.remove(next_word)

        return 0