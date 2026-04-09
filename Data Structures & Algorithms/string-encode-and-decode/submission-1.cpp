class Solution {
public:
    string encode(vector<string>& strs) {
        string encoded = "";
        for (int i = 0; i < strs.size(); i++) {
            encoded += to_string(strs[i].size()) + "#" + strs[i];
        }
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int index = 0;
        int length = s.size();
       while(index < length ){
        int hashIndex = index ;
        while(s[hashIndex] != '#' ){
            hashIndex++;
        }
        int lengthOfDecoded = stoi(s.substr(index, hashIndex - index ));
        cout<<lengthOfDecoded <<"here";
        index = hashIndex + 1 ;
        string decoded = s.substr(index, lengthOfDecoded);
        res.push_back(decoded);
        index = index + lengthOfDecoded ;
       }

        return res;
    }
};
