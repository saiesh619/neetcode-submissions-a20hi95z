class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countOfS = [0]*26 
        countOfT = [0]*26 
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            countOfS[ord(s[i]) - ord('a')]+= 1
            countOfT[ord(t[i]) - ord('a')]+= 1
                
        return countOfS == countOfT