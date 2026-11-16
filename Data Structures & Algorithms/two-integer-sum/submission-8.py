class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = Counter()

        for i in range(len(nums)):
            com = target - nums[i]            
            if com in freq:
                return [freq[com],i]
            freq[nums[i]] = i
        
        return []