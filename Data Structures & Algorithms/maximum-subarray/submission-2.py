class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s, r = 0, nums[0]
        for n in nums:                      
            if s < 0:
                s = 0
            s += n  
            r = max(r,s)
        return r