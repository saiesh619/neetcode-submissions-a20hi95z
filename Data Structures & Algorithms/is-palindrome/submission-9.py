class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s) - 1
        index = 0
        parsedString = ""
        while index <= right:
            value = s[index]
            if value.isalnum():
                parsedString += s[index]
            index += 1
        print(parsedString)
        right = len(parsedString) - 1
        while left < right:            
            if str.lower(parsedString[left]) != str.lower(parsedString[right]):                
                print
                return False
            left += 1
            right -= 1
        return True