class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
         map<string,vector<string>> mappingOfSorted;
        vector<vector<string>> result ;
        for(int i = 0 ; i < strs.size() ; i ++){
            vector<int> freq(26,0);
            string sorted = strs[i] ;
            string key = "";
            for(char i : strs[i]){
                freq[i -'a']++;                
            }
            for (int num : freq) {            
            key = key + to_string(num) + "," ;
        }

            mappingOfSorted[key].push_back(strs[i]);
        }
     
          for (auto& pair : mappingOfSorted) {
            result.push_back(pair.second);
        }
        return result ;

        
         
    }
};
