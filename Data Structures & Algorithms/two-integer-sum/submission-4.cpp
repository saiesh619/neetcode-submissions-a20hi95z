class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans ;
        unordered_map<int,int> complement;
        int n = nums.size();
        for(int i = 0 ; i < n ; i++){
            int c = target - nums[i];
            
            if(complement.count(nums[i])){
                cout<<"here";
               ans.push_back(complement[nums[i]]);
               ans.push_back(i);
               return ans;
            }
            complement[c] = i;
        }
        return ans;
    }
};
