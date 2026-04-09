

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        preProd = [1] * n
        postProd = [1] * n
        res = [1] * n
        p = 1
        preProd[0] = 1
        postProd[n - 1] = 1
        

        for i in range(len(nums) - 2,-1, -1):
            postProd[i] = postProd[i + 1] * nums[i + 1] 
        
        for i in range(1,len(nums)):
            p = p * nums[i - 1] 
            postProd[i] = p * postProd[i]
            print(i," \npostProd[i] * nums[i - 1]", postProd[i])
       
        return postProd
         
    