class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0
        length = 0
        for numbers in numSet:
            if (numbers - 1) not in numSet:
                length = 1
                while (numbers + length) in numSet:
                    length = length + 1
                    print(numbers + length ,"\n")
            maxLength = max(length,maxLength) 

        return maxLength   


        