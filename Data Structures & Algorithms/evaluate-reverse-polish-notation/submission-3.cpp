class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st ;
        int result = 0 ;
        for(int i = 0 ; i < tokens.size() ; i++){
           
            if(tokens[i]=="+" || tokens[i]=="-" || tokens[i]=="*"||tokens[i]=="/"){
                int second = st.top();
                st.pop();
                int first = st.top();
                st.pop();
                int result ;
                if(tokens[i]=="+"){
                    result = first + second ;
                }
                else if(tokens[i]=="-"){
                    result = first - second;
                }
                else if(tokens[i]=="*"){
                    result = first * second;
                }
                else if(tokens[i]=="/"){
                    result = first / second;
                }
                st.push(result);                
        }
        else{
            st.push(stoi(tokens[i]));
        }
        }
        return st.top();
    }
};
