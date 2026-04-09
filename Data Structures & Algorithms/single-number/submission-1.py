class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x  = nums[0]
        n = len(nums)
        for i in range(1,n): 
            x = x^nums[i]
        return x