class Solution(object):
    def threeSum(self, nums):
        left = 0         
        nums.sort()
        res = []
        print(nums)
        for i in range(len(nums) - 2):                
            if i > 0 and nums[i] == nums[i - 1]:
                continue        
            first = nums[i]
            left = i + 1
            right = len(nums) - 1            
            while left < right:
                target = first + nums[left] + nums[right]                              
                if target < 0 :
                    left += 1                    
                elif target > 0 :
                    right -= 1
                elif target == 0 :
                    res.append([first,nums[left],nums[right]])
                    left+= 1
                    right-= 1    
                    while left < right and nums[left] == nums[left - 1]:
                        left+= 1                                            
                    while right >= 0 and nums[right] == nums[right + 1]:
                        right-= 1

        return res
        