
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        
        for(auto ch:tokens){
            if(ch == "+" or ch == "-" or ch == "/" or ch == "*"){
                int first = st.top();
                st.pop();
                int second = st.top();
                st.pop();
                if(ch == "+"){
                    cout<<first  ;
                    cout<<" "<<second;
                    st.push(first + second);
                }               
                if(ch == "-"){
                   
                    st.push(second - first);
                }
                else if(ch == "*"){
                    st.push(first*second);
                }
                else if(ch == "/"){
                    st.push(second/first);
                }
            }
            else{
                st.push(stoi(ch));
            }
        }

        return st.top();
        
    }
};
