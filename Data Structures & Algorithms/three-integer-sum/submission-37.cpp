class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int left = 0 ;
        int right = nums.size() - 1 ;
        vector<vector<int>> res ;
        sort(nums.begin(),nums.end());
        int n = nums.size() ;
        for(int i = 0 ; i < n ; i++){
            if( i > 0 and nums[i - 1] == nums[i]){
                continue ;
            }
            left = i + 1 ;
            right = nums.size() - 1 ;
            while(left < right){
                int ans = nums[i] + nums[left] + nums[right];
                if(ans > 0){
                    right -= 1;
                }
                else if(ans < 0){
                    left += 1;
                }
                else{
                    res.push_back({nums[i], nums[left], nums[right]});
                    left += 1;
                    right -= 1;
                    while(left < right and nums[left] == nums[left - 1]){
                        left += 1 ;
                    }
                    while(left < right and nums[right] == nums[right + 1]){
                        right -= 1 ;
                    }
                }

            }
        }
        return res;
    }
};
