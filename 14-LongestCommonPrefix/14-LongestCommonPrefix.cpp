// Last updated: 6/12/2025, 8:28:22 PM
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
    string x { };
        if (strs.empty()){return "";}
        for( int i=0;i<(strs[0].size());i++)
        {

            char c=strs[0][i];
            for (int j=1;j<strs.size();j++)
            {
                if ((i==strs[j].size()) || (strs[j][i]!=c))
                {
                    x= strs[0].substr(0,i);
                    return x;
                }
            }


        }
        return strs[0];
        
    }
};