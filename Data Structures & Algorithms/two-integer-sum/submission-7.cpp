class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res ;
        unordered_map<int,int> complement;
        int n = nums.size();
        for(int i = 0 ; i < n ; i++){
            int c = target - nums[i];
            if(complement.contains(nums[i])){                
                res.push_back(complement[nums[i]]);
                res.push_back(i);
                return res;
            }
            complement[c] = i;
        }
        return res;
    }
};
