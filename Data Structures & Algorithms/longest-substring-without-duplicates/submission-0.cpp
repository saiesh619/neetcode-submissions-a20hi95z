class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int right = 0 ;
        int left = 0 ;
        set<char> previousChar;
        int maxLength = 0 ;
        for(right = 0 ; right < s.size() ; right++){   
                   
            while(previousChar.find(s[right])!=previousChar.end()){
                previousChar.erase(s[left]);
                left++;
            }
            cout<<s[right]<<endl;
            maxLength = max(maxLength,right - left + 1); 
            previousChar.insert(s[right]);            
        }
        return maxLength;
    }
};
