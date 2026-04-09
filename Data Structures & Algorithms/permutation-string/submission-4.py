class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        Cs1 = [0] * 26
        Cs2 = [0] * 26
        l = 0
        r = 0
        if len(s1) > len(s2):
            return False
        
        for i in range(len(s1)):
            Cs1[ord(s1[i]) - ord('a')] += 1
            Cs2[ord(s2[i]) - ord('a')] += 1

        if Cs1 == Cs2 :
            return True

        for r in range(len(s1), len(s2)):
            Cs2[ord(s2[r]) - ord('a')] += 1
            Cs2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            if Cs2 == Cs1:
                return True
        
        return False