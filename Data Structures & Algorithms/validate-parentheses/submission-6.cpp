
class Solution {
public:
    bool isValid(string s) {
        stack<char> st ;
        if(s.size() % 2){
            return false;
        }
        for(char ch : s){
            if(ch == '[' or ch == '{' or ch == '('){
                st.push(ch);
            }
            else{
                if(st.empty()){
                    return false;
                }
                if(ch == '}' and st.top() != '{'){
                    return false;
                }
                if(ch == ']' and st.top() != '['){
                    return false;
                }
                if(ch == ')' and st.top() != '('){
                    return false;
                }
                
                else{
                    st.pop();
                }
            }
            
            
        }
        return st.empty();
    }
};
