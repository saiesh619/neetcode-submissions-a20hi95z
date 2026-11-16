class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [[] for _ in range(n + 1)]
        topK = []
        bucket = Counter(nums)

        for value, count in bucket.items():
            res[count].append(value)


        for item in reversed(res):
            for v in item:
                topK.append(v)
            
            if len(topK) == k:
                return topK
        
        return topK


        
        











