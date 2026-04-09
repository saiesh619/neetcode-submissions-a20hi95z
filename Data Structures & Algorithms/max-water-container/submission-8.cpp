class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0 ;
        int right = heights.size() - 1 ;
        int ans = 0 ;
        while(left < right){
            int h = min(heights[left], heights[right]);
            ans = max(ans, (right - left) *h);
            if(heights[left] > heights[right]){
                right -= 1 ;
            }
            else{
                left += 1;
            }
        }
        return ans;
    }
};
