class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)
        for x,y in points:
            dist = x**2 + y**2
            heapq.heappush(minHeap,[dist,x,y])
        ans = []
        while k > 0:
            
            dist,x,y = heapq.heappop(minHeap)
            
            ans.append([x,y])
            k -= 1
        return ans
