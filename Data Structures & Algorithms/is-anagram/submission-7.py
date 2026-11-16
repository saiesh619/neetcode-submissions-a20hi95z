class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = Counter(s)
        freqT = Counter(t) 
        if freqT == freqS:
            return True
        
        return False