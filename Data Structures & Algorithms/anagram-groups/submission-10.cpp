class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> group;
        vector<vector<string>> res;

        for(const auto &word: strs){
            int len = word.size();
            vector<int>letter(26);
            for(int i = 0 ; i < len ; i++){
                letter[word[i] - 'a'] += 1;
            }
            string key = "";
            for(int i = 0 ; i < 25; i++){
                key += to_string(letter[i]) + ",";
            }
            group[key].push_back(word);
        }
        for(const auto &entry : group){
            res.push_back(entry.second);
        }
        return res;
    }
};
