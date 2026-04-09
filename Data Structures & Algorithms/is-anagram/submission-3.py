class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        freqS = defaultdict(int)
        freqT = defaultdict(int)
        if len(s) != len(t):
            return False

        for c in s:
            freqS[c] += 1
        
        for ch in t:
            freqT[ch] += 1

        if freqT != freqS:
            return False
        return True