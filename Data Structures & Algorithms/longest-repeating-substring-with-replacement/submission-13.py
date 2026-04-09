#Algorithm
#1. Keep a track of left and right pointer
#2. Left = 0 and right = 0
#3. Expand the right window one char at a time and add it to freq map & keep track of maxFreq char
#4. Size of map > 1, then do : k - maxFreq  
#5. 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left = 0
        n = len(s)
        maxCount = 0
        leng = 0
        for right in range(n):
            freq[s[right]] += 1
            maxCount = max(maxCount, freq[s[right]])
            while right - left + 1 - maxCount > k :
                freq[s[left]]-= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            
            leng = max(right - left + 1, leng)
        
        return leng