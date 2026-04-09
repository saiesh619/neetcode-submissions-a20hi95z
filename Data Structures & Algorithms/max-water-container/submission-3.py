class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        maxArea = 0 
        while left < right:            
            length = right - left 
            area = length * min(heights[left],heights[right])
            print("lenght \n", length)
            print("height \n", min(heights[left],heights[right]))
            maxArea = max(area,maxArea)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea