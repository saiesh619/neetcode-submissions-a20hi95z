class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return []
        digitToChar = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def backtrack(i,curStr):
            if i == len(digits):
                res.append(curStr)
                return 
            
            s = digitToChar[digits[i]]

            for char in s:                
                backtrack(i + 1, curStr + char)


        backtrack(0, "")
        return res

        

        