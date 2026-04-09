class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> groups;
        vector<vector<string>> res;
        for(string word : strs){
            int n = word.size();
            vector<int> letters(26);

            for(int i = 0 ; i < n ; i++){
                letters[word[i] - 'a'] += 1 ;
            }
            string key = "";
            for(int x : letters){
                key += to_string(x) + ",";
            }
            groups[key].push_back(word);
        }
        for(const auto &value : groups){
            res.push_back(value.second);
        }
        return res;
    }
};
