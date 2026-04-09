class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        int sL = s.size();
        int tL = t.size();
        if(sL != tL){
            return false;
        }
        cout<<"here "<<s;
        if(s == t){
            cout<<s;
            return true;
        }
        return false;
    }
};
