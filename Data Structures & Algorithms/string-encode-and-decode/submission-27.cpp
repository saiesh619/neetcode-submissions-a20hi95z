class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded = "";

        for(int i = 0 ; i < strs.size() ; i++){
            encoded += to_string(strs[i].size()) + "#" + strs[i]; 
        }

        return encoded ;

    }

    vector<string> decode(string s) {
        vector<string> decoded ;
        int i = 0 ;
        int j = 0 ;
        int n = s.size();
        while(i < n){
            j = i ;
            while(s[j] != '#'){
                j += 1;
            }
            int len = stoi(s.substr(i,j-i));
             i = j + 1 ;
             j = i + len ;
            decoded.push_back(s.substr(i,len));
            i = j;
        }
    
        return decoded;
    }
};
