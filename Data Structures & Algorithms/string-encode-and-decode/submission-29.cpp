class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded = "";
        for(int i = 0 ; i < strs.size();i++){
            encoded += to_string(strs[i].size()) + "#" + strs[i];
        }
        
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> decoded ;
        int i, j ;
        i = 0 ;
        int n = s.size();
        while(i < n){
            j = i ;
            int len ;
            while(s[j] != '#'){
                j += 1 ;
            }    
            len = stoi(s.substr(i,j - i));
            cout<<len;
            i = j + 1 ;
            j = i + len ;
            cout<<"ans "<<s.substr(i,j);
            decoded.push_back(s.substr(i,len));
            i = j;
        }
        return decoded;
    }
};
