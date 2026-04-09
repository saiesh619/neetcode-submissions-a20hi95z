class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        longest = 0
        l = 0
        r = 0
        ans = 0
        for i in range(len(s)):
            count[ord(s[i]) - 65] += 1
            while (i - l + 1) - max(count) > k:
                count[ord(s[l]) - 65] -= 1
                l += 1
            ans = max(ans, i - l + 1)
        return ans
