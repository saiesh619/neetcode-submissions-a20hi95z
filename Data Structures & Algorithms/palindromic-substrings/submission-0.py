class Solution:
    def countSubstrings(self, s: str) -> int:
        l = 0
        r = 0 
        resStart = 0
        resLen = 0
        ans = 0
        for i in range(len(s)):

            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                if r - l + 1 > resLen:
                    resStart = l
                    resLen = r - l + 1
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                if r - l + 1 > resLen:
                    resStart = l
                    resLen = r - l + 1
                l -= 1
                r += 1
        return ans
        