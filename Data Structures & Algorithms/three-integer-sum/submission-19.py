class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left,right = i+1, len(nums) - 1

            while left < right:
                s = nums[left] + nums[right] + nums[i]

                if s > 0:
                    right -= 1
                
                elif s < 0:
                    left += 1

                else:
                    res.append([nums[left],nums[right],nums[i]])
                    left += 1
                    right -= 1                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        
        return res