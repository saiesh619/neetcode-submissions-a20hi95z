class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> setOfnums;
        for(int i : nums){
            setOfnums.insert(i);
        }
        int index = 0 ;
        int res = 0 ;
        while(index < nums.size()){
            if(setOfnums.find(nums[index] - 1)== setOfnums.end()){
                int startOfSequence = nums[index];
                int count = 1 ;                
                int nextValueInSequence = startOfSequence + 1 ;
                while(setOfnums.find(nextValueInSequence) != setOfnums.end()){
                    nextValueInSequence = nextValueInSequence + 1 ;
                    count++ ;
                }
                res = max(count,res);
                
            }
            index++;
        }
        return res ;
        
    }
};
