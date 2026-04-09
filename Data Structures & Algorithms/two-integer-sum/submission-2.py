class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap ={}
        for i in range(len(nums)):
            ans = (target - nums[i])     
            print(ans)
            print(hmap)
            if ans in hmap:
                index = hmap[ans]
                return [index,i]
            else:
                hmap[nums[i]] = i
        
        return []


        [3,4,5,6]
        a = 7 - 3
        a = 4
        h[0] = 3 / a[i]

        a = 7 - 4
        h[1] = 3

