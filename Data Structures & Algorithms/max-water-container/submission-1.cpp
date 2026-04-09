class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0 ;
        int right = heights.size() - 1;
        int res = 0;
        int area ;
        while(left < right){            
            area = min(heights[left],heights[right]) * (right - left);
            if(heights[left] < heights[right]){
                left++ ;
                cout<<heights[left]<<" left ";
                cout<<heights[right-1]<<" right ";
            }
            else {
                right-- ;
            }
            
            res = max(area,res);
        
        }        
        return res;
    }
};
