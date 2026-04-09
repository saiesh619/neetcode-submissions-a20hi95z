

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> freq;
        int n = nums.size();
        vector<vector<int>>bucket(n + 1);
        vector<int>res;
        for(int x : nums){
            freq[x] += 1;
        }
        for(const auto &entry : freq ){
            int f = entry.second;
            int x = entry.first;
            bucket[f].push_back(x) ;
        }
        
        for(int i = n ; i >= 0 ;i--){
                for(int element : bucket[i]){
                    res.push_back(element);
                
                if(res.size() == k){
                    return res;
                }
                }
            }
           
    
        return res;
    }

    
};
