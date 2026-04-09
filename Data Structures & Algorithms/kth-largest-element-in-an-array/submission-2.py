class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for element in nums:
            
            heapq.heappush(heap,element)
            if len(heap) > k :
                heapq.heappop(heap)

        return heap[0]

