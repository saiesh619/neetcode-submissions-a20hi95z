class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        check = set()
        maxCount = 0
        for r in range(len(s)):
            
            print([r])
            print([l])
            while s[r] in check:
                check.remove(s[l])
                l += 1
            check.add(s[r])
            maxCount = max(maxCount, r - l + 1)
        return maxCount
