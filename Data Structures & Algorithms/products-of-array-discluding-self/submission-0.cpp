class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res(nums.size());
        res[0] = 1;
        for(int i = 1 ; i < nums.size() ; i++){
            res[i] = nums[i-1]*res[i - 1];
        }
        int p = 1 ;
        for(int i = nums.size() - 2 ; i >=0 ; i--){
            p = p * nums[i+1];
            res[i] = res[i] * p;
        }
        return res;
    }
};
