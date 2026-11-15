#return type : boolean
# input is an array
# n = 0 ; false
# n = 0 -> some big number
# 

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        print(freq)
        for key,value in freq.items():
            if value > 1 :
                return True
        return False 