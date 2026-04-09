class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 0
        characters = set()
        maxcount = 0
        count = 0
        while left < len(s) and right < len(s):
            while right < len(s) and s[right] not in characters :
                characters.add(s[right])
                right+=1
            length = right - left           
            maxcount = max(length , maxcount)
            characters.remove(s[left])
            left += 1

        return maxcount 
            