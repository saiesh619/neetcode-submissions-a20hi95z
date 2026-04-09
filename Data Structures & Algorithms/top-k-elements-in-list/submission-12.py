class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqOfElements = {}
        bucket = {}
        res = []

        for num in nums:
            freqOfElements[num] = freqOfElements.get(num, 0) + 1

        for num, freq in freqOfElements.items():
            if freq not in bucket:
                bucket[freq] = []
            bucket[freq].append(num)

        for i in range(len(nums), 0, -1):  # Go from max possible freq
            if i in bucket:
                for num in bucket[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
        return res
