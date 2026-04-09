class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0 ;
        int right = heights.size() - 1 ;
        int maxArea = 0 ;
        while(left < right){                
            int length = right - left;            
            int height = min(heights[left],heights[right]);
            cout<<length<<" "<<height<<endl;
            int area = length * height ;      
            maxArea = max(area,maxArea);
            if(heights[left] < heights[right]){
                left ++;
            }  
            else{
                right --;
            }
            
    }
    return maxArea ;
    }
};
