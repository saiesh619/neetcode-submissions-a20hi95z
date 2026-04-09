class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int left = 0 ;
        int right = nums.size() - 1 ;
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        for(int i = 0 ; i < right ; i++){
            left = i + 1;
            right = nums.size() - 1 ;
            if( i > 0 && nums[i] == nums[i-1]){
                continue ;
            }
            
            while(left < right){
                int s = nums[i] + nums[left] + nums[right];
                cout<<"s "<<s<<endl ;
                if(s > 0){
                    right -= 1;
                }
                else if(s < 0){
                    left += 1;
                }
                else{
                    res.push_back({nums[i],nums[left],nums[right]});
                    left += 1 ;
                    right -= 1;
                    while(left < right && nums[left] == nums[left - 1]){
                        left += 1;
                    }
                     while(left < right && nums[right] == nums[right + 1]){
                       right -= 1;
                    }
                }
                
            }
        }
        return res;
    }
};
