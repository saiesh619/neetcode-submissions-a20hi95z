class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        def dfs(index, s, sub):
            if index >= len(nums):
                return
            if s == target:
                res.append(sub.copy())
                return
            if s > target:
                return 
            
            sub.append(nums[index])
            dfs(index,s + nums[index],sub)
            sub.pop()
            dfs(index + 1,s,sub)
        dfs(0,0,sub)
        return res