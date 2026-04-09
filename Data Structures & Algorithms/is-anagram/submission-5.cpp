class Solution {
public:
    bool isAnagram(string s, string t) {
       unordered_map<char,int>countT;
       unordered_map<char,int>countS;
        int sL = s.size();
        int tL = t.size();
        if(sL != tL){
            return false;
        }

        for(int i = 0 ; i < sL ; i++){
            char characterS = s[i];
            char characterT = t[i];
            countT[characterS] += 1 ; 
            countS[characterT] += 1 ;         
            
        }

        for(int i = 0 ; i < sL ; i++){
            char character = s[i];
            if(countT[character] != countS[character]){
                return false;
            }
        }
      
       return true;
    }
};
