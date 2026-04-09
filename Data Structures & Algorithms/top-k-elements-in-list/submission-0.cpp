class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> freq ;
        vector<vector<int>> count(nums.size() + 1) ;
        for(int i = 0 ; i < nums.size() ; i++){
            freq[nums[i]]++;
        }
        for(const auto&entry:freq){
            count[entry.second].push_back(entry.first);
        }
        vector<int> res;
        for(int i = count.size() - 1 ; i >0 ; i--){
            for(int n: count[i]){
                res.push_back(n);
                if(res.size()==k){
                    return res;
                }
            }
        }
        return res ;
    }
        
        
    
};
