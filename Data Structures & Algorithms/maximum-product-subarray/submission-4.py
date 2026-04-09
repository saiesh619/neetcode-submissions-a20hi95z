class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cmin = 1
        cmax = 1
        
        for num in nums:
            ans = cmax * num
            cmax = max(ans, cmin * num, num)
            cmin = min(ans,cmin * num, num)
            res = max(res,cmax)
        return res
