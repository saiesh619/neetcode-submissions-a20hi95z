class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        maxCount = 0
        for n in nums:
            prev = n - 1
            if prev not in check:
                seq = n
                count = 0
                while seq in check:
                    seq += 1
                    count += 1
                maxCount = max(count,maxCount)

        return maxCount