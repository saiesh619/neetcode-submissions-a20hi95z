class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        k = len(nums) - k + 1
        while k > 0 :
            ans = heapq.heappop(nums)
            k -= 1
        print(ans)
        return (ans)