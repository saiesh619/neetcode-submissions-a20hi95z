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
        
        while (index < s.size()) {
            int j = index;
            // Find the '#' to get length of next word
            while (s[j] != '#') {
                j++;
            }

            int lengthOfEncoded = stoi(s.substr(index, j - index));
            index = j + 1; // move past '#'

            string decoded = s.substr(index, lengthOfEncoded);
            res.push_back(decoded);

            index += lengthOfEncoded; // move to next encoded string
        }

        return res;
    }
};
