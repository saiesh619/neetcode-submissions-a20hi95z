class Solution {
public:

    string encode(vector<string>& strs) {
        string encode = "";
        for(int i = 0 ; i < strs.size() ; i++){
            encode += to_string(strs[i].size()) + "#" + strs[i];
        }
        return encode;
    }

    vector<string> decode(string s) {
        vector<string> decoded ;
        int n = s.size();
        int i = 0 ;
        int j;
        while(i < n){
            int len ;
            j = i ;

            while(s[j] != '#'){
                j += 1;
            }
            len = stoi(s.substr(i , j - i));
                             
            i = j + 1 ;
            j = len + i;
            cout<<" j = "<<j<<endl;
            cout<<s[j];
            decoded.push_back(s.substr(i,len));
            i = j;
        }
        return decoded;
    }
};
