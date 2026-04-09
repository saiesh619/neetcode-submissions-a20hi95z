class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> freq;
        vector<vector<int>> count(nums.size() + 1);
        for(int i = 0 ; i < nums.size() ; i++){
            freq[nums[i]]++;
        }  
        vector<int> res;
        for (const auto& pair : freq) {
            count[pair.second].push_back(pair.first) ;            
        }
        
         
        for(int i = count.size() - 1 ; i > 0 ; i--){            
            for(int n : count[i]){
                res.push_back(n);
                if(res.size() == k){
                    return res;
                }
            }
        }
        return res;
    }
};
