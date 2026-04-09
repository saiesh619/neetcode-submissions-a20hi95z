class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int>freq;        
        vector<int> res;
        int n = nums.size();
        vector<vector<int>>bucket(n+1);
        for(int x :nums){
            freq[x] += 1;
        }
        for(const auto & entry:freq){
            int va = entry.first;
            int f = entry.second;
            bucket[f].push_back(va) ; 
        }

        for(int i = n  ; i >= 0 ; i--){
            cout<<"element";
            //cout<<bucket[i];
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
