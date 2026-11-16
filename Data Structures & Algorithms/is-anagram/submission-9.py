class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = [0]*26
        freqT = [0]*26
        
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            freqS[ord(s[i]) - ord('a')] += 1
            freqT[ord(t[i]) - ord('a')] += 1
        
        if freqT == freqS:
            return True
        
        return False


