class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> group;
        vector<vector<string>> ans ;
        for(auto &word : strs){
            vector<int> letters(26);

            for(int i = 0 ; i < word.size() ; i++){
                letters[word[i] - 'a'] += 1;
            }
            string key = "";
            for(int i = 0 ; i < 26 ; i++){
                key += to_string(letters[i]) + ",";
            }
            group[key].push_back(word);
        }
        for(auto &entry : group){
            ans.push_back(entry.second);
        }
        return ans;
    }
};
