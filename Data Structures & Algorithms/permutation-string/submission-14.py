class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqS1 = defaultdict(int)
        freqS2 = defaultdict(int)
        index = 0
        left = 0
        if len(s1) > len(s2):
            return False

        while index < len(s1):
            freqS1[s1[index]] += 1
            freqS2[s2[index]] += 1
            index += 1
        
        if freqS1 == freqS2:
            return True
        
        for right in range(index,len(s2)):
            freqS2[s2[right]] += 1
            freqS2[s2[left]] -= 1
            
            if freqS2[s2[left]] == 0:
                del freqS2[s2[left]]
            
            if freqS1 == freqS2:
                return True

            left += 1
        return False