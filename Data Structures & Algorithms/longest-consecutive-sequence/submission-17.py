class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequenceChecker = set()
        length = len(nums)
        index = 0
        count = 0
        maxCount = 0
        for values in nums:
            sequenceChecker.add(values)
        while index < length:
            value = nums[index]
            if value - 1 not in sequenceChecker:
                count = 1
                while value + 1 in sequenceChecker:                
                    count += 1
                    value = value + 1
                maxCount = max(count,maxCount)
            index += 1
        return maxCount


        