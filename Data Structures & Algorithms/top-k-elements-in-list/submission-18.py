
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        n = len(nums) + 1
        bucket = [[] for _ in range(n)]
        res = []
        for key,value in freq.items():
            bucket[value].append(key)
        
        for i in range(n - 1,-1,-1):
            if k == 0:
                break
            for x in bucket[i]:
                res.append(x)
                k = k - 1
        return res
        