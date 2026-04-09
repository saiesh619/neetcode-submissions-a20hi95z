class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        output = []
        left = 0
        right = 0
        n = len(nums)

        while right < n :
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            if left > q[0]:
                q.popleft()
            
            if (right+1) >= k:
                output.append(nums[q[0]])
                left += 1
            right += 1
        return output
                
