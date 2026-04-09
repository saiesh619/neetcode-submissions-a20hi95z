class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
     vector<vector<int>> res ;
     int left = 0 ;
     int right = nums.size() - 1 ;
     int n = nums.size();
     sort(nums.begin(), nums.end());
     for(int i = 0 ; i < n ; i++){
        if(i > 0 && nums[i - 1] == nums[i]){
            continue;
        }
        left = i + 1 ;
        right = nums.size() - 1;
        while(left < right){
            int x = nums[i] + nums[left] + nums[right];

            if(x < 0){
                left += 1;
            }
            else if(x > 0) {
                right -= 1;
            }
            else{
                res.push_back({nums[i],nums[left],nums[right]});
                left += 1 ;
                right -= 1 ;

                while(left < right and nums[left] == nums[left - 1]){
                    left += 1;
                }
                
                while(left < right and nums[right] == nums[right + 1]){
                    right -= 1;
                }
            }
        }
      
     }   
       return res;
    }
};
