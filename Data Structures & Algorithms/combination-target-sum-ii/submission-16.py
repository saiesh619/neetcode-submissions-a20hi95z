class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        candidates.sort()
        def dfs(index, s,sub):                        
            if s == target:
                res.append(sub.copy())
                return
            
            if index >= len(candidates) or s > target:
                return
                                   
            sub.append(candidates[index])
            dfs(index + 1, s + candidates[index],sub)
            sub.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            dfs(index + 1, s,sub )
        
        dfs(0,0,[])
        return res
        