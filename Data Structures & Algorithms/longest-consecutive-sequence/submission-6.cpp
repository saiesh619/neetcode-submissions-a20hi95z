class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> elements;
        for(int i : nums){
            elements.insert(i);
        }
        int count = 0 ;
        int res = 0;
        int i = 0;
        while(i < nums.size()){
            if(elements.find(nums[i] - 1) == elements.end()){ 
                int x = nums[i];               
                while(elements.find(x) != elements.end()){
                    count++ ;
                    x = x + 1 ;
                    cout<<" x "<<x;
                    cout<<endl;
                
                }
            }
                i++;
                res = max(res,count);
                count = 0;
        }
            
          
           
        
        return res;
    }
    
};
