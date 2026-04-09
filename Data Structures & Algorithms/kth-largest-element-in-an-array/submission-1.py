class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for element in nums:
            heapq.heapify(heap)
            heapq.heappush(heap,element)
            if len(heap) > k :
                heapq.heappop(heap)

        return heap[0]

