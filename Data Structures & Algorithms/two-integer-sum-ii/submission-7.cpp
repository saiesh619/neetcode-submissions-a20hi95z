class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0 ; 
        int right = numbers.size() - 1;
        int s = 0 ;
        vector<int> res ;
        sort(numbers.begin(), numbers.end());
        while(left < right){
            int x = numbers[left] + numbers[right];
            if(x < target){
                left += 1;
            }
            else if(x > target){
                right -= 1;
            }
            else{
                res.push_back(left + 1);
                res.push_back(right + 1);
                return res;
            }
        }
        return res;
    }
};
