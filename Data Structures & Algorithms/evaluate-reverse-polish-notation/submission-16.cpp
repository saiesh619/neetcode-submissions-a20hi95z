class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> res ;
        int n = tokens.size();
        for(int i = 0 ; i < n ; i++){
            if(tokens[i] == "+"){
             int n1 = res.top();
             res.pop();
             int n2 = res.top();
             res.pop();
             res.push(n1 + n2);
            }
            else if(tokens[i] == "-"){
            int n1 = res.top();
             res.pop();
             int n2 = res.top();
             res.pop();
             res.push(n2 - n1);
            }
            else if(tokens[i] == "*"){
            int n1 = res.top();
             res.pop();
             int n2 = res.top();
             res.pop();
             res.push(n1 * n2);
            }
            else if(tokens[i] == "/"){
                int n1 = res.top();
             res.pop();
             int n2 = res.top();
             res.pop();
             res.push(n2 / n1);
            }
            else{
                res.push(stoi(tokens[i]));
            }
        }
        return res.top();
    }
};
