class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        left = 0 
        n = len(s)
        maxCount = 0
        for right in range(n):
            element = s[right]
            freq[element] += 1
            while freq[element] != 1 :
                freq[s[left]] -= 1
                left += 1
            maxCount = max(maxCount, right - left + 1)
        return maxCount