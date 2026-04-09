class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        vector<vector<int>> bucket(n + 1);
        vector<int> res ;
        unordered_map<int,int> freq;
        for(int i = 0 ; i < n ; i++){
            freq[nums[i]] += 1 ;
        }
        for(const auto &entry:freq){
            int v = entry.first;
            int f = entry.second ;
            bucket[f].push_back(v) ;
        }
        for(int i = n ; i >= 0 ; i--){
            for( int entry:bucket[i]){
                res.push_back(entry);
                if(res.size() == k){
                    return res;
                }
            }
        }
        return res;
    }
};
