class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> groups;
        for(int i = 0 ; i < strs.size() ; i++){
            vector<int>count(26,0) ;
            string word = strs[i] ;
        for(int i = 0 ; i < word.size() ; i++){
            count[word[i] - 'a']++;
            }
        string key ;
        key = to_string(count[0]);
        for(int i = 1 ; i < 26  ; i++){
            key += ',' + to_string(count[i]); 
            }
            cout<<"key "<<key;
            groups[key].push_back(word);  
            
        }   
        vector<vector<string>>res ;   
        for(const auto& pair: groups){
            res.push_back(pair.second);
        }
        return res; 
}
};
