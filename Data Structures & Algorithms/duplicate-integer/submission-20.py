#return type : boolean
# input is an array
# n = 0 ; false
# n = 0 -> some big number
# 

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for v in nums:
            if v in seen:
                return True
            seen.add(v)

        return False