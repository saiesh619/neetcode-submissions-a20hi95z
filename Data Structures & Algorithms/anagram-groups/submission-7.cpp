class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
      unordered_map<string,vector<string>> groups;
        vector<vector<string>> res ;
        for(auto &word:strs){
            int n = word.size();
            vector<int> letters(26) ;
            for(int i = 0 ; i < n ; i++){
                letters[word[i] - 'a'] += 1 ;
            }
            string key = "";
            for(int count : letters){
                key += to_string(count) + ",";
            }
            groups[key].push_back(word);

           
        }
         for(auto &entry:groups){
                res.push_back(entry.second);
            }
        return res;
        }
    
        
};
