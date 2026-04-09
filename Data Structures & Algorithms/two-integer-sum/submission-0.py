class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousElements = {}
        result = []
        for i in range(len(nums)):
            s = target - nums[i] 
            if s in previousElements:
                return [previousElements[s],i]
            else:
                previousElements[nums[i]] = i
        print(previousElements)
        return []
        