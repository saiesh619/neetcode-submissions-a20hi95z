class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        a = 1
        b = 1
        c = 0
        for i in range(1,len(s)):
            curr = 0
            if s[i] != '0':
                curr += a 
            digit = int(s[i-1:i+1])
            if digit >= 10 and digit <= 26:
                curr += b
            a,b = curr,a
        return a
        