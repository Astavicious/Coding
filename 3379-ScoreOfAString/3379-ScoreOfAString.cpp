// Last updated: 6/12/2025, 8:27:44 PM
class Solution {
public:
    int scoreOfString(string s) {
        int x=0;
        for(int i=0;i<s.size()-1;i++)
        {
            int k=(int)s[i];
            int l=(int)s[i+1];
            x+=abs(l-k);
        }
        return x;
    }
};