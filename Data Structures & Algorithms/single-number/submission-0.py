class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for bit in nums:
            res = bit ^ res
        return res