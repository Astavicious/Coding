// Last updated: 6/12/2025, 8:28:17 PM
class Solution {
public:
    int lengthOfLastWord(string s) {
        int i=s.size()-1;
        int count{0};
        while(s[i]==' ')
        {
            i--;
        }
        for(int j=i;j>=0;j--)
        {
            if(s[j]!=' ')
            {
                count++;
            }
            else{
                break;
            }
        }
        return count;
    }
};