class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res ;
        backtrack("",n,n,n,res);    
        return res ;    
    }
    void backtrack(string brackets, int length, int open, int close,vector<string>&res){ 
        if(open == 0 && close == 0){
            res.push_back(brackets);
            return ;
        }
        if(open > 0){            
            backtrack(brackets + '(',length, open - 1, close,res);                        
        }
        if(open < close){            
            backtrack(brackets + ')',length, open, close - 1,res);                        
        }
    }
};
