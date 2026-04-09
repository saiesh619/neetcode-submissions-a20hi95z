

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int>seen;
        int count = 0;
        int ans = 0 ;
        for(int x : nums){
            seen.insert(x);
        }
        for(int x : nums){
            count = 1;
            if(seen.count(x-1)){
                
                while(seen.count(x)){
                    count += 1;
                    x = x + 1;
                }
            }
                ans = max(ans,count);
            
        }
        return ans;
    }
};
