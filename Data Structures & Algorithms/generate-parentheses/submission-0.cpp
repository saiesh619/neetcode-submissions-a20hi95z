class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        backtrack("", n, n, res);    
        return res;    
    }

    void backtrack(string brackets, int open, int close, vector<string>& res) { 
        if (open == 0 && close == 0) {
            res.push_back(brackets);
            return;
        }

        if (open > 0) {            
            backtrack(brackets + '(', open - 1, close, res);                        
        }

        if (close > open) {            
            backtrack(brackets + ')', open, close - 1, res);                        
        }
    }
};
