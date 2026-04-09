class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set <int> numSet(nums.begin(), nums.end());
        int length ;
        int maxLength = 0;
        for(auto nums: numSet ){
            if(numSet.find(nums - 1) == numSet.end()){
                length = 1 ;
                while(numSet.find(nums + length) != numSet.end()){
                    length ++;
                }
                maxLength = max(maxLength,length);
            }
        }
        return maxLength;
    }
};
