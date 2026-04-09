// keep a stack
//inside loop do the following :
// push the first elemeent's omdex
// traverse the array until you find an element greater than the current top of the stack
// if greater find the difference between indexes of current element and the top element
// if not greater than push to stack
// repeat

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> temp ;
        int n = temperatures.size();
        vector<int> res(n);
        for(int i = 0 ; i < n ; i++){ 
                while(!temp.empty() and temperatures[temp.top()] < temperatures[i]){
                
                    res[temp.top()] = (i - temp.top());
                    temp.pop();
                    
                }
                temp.push(i);
            }
                
        
        return res;
    }
};
