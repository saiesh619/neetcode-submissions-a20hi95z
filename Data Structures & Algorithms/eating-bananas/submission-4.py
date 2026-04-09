class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low  = 1
        high = max(piles)
        res = high
        while low <= high:
            mid = low + (high - low) // 2
            time = 0
            for ban in piles:
                time += (ban + mid - 1) // mid            
            if time > h:
                low = mid + 1
                
            else:
                res = mid
                high = mid - 1
        return res