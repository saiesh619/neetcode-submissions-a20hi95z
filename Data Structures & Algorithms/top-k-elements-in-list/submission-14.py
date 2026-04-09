class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqOfElements = {}
        bucket = {}
        res = []

        for values in nums:
            freqOfElements[values] = freqOfElements.get(values,0) + 1
        
        for key,freq in freqOfElements.items():
            if freq not in bucket:
                bucket[freq] = []
            bucket[freq].append(key)
        
        print(k)
        print(len(res))
        for i in range(len(nums),0,-1):             
            if i in bucket:
                for nums in bucket[i]:
                    res.append(nums)
                if len(res) == k:
                    return res

        return []