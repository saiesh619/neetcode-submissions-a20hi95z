class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
         map<string,vector<string>> mappingOfSorted;
        vector<vector<string>> result ;
        for(int i = 0 ; i < strs.size() ; i ++){
            map<char,int>freq ={};
            string sorted = strs[i] ;
            string key = "";
            for(char i : sorted){
                freq[i]++;             
            }
            for (auto& pair : freq) {                    
                key = key + pair.first + to_string(pair.second) + ",";
        }

            mappingOfSorted[key].push_back(sorted);
        }
     
          for (auto& pair : mappingOfSorted) {
            result.push_back(pair.second);
        }
        return result ;  
    }
};
