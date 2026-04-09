class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        r = nums[0]
        for n in nums:
            if s < 0 :
                s = 0
            s += n
            r = max(s,r)
        return r