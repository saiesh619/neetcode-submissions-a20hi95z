class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueValues = set(nums)
        maxLength = 0
        for v in nums:
            if (v - 1) not in uniqueValues:
                sequence = 0
                startValue = v
                while(startValue in uniqueValues):
                    startValue += 1
                    sequence += 1

                maxLength = max(sequence,maxLength)            

        return maxLength 