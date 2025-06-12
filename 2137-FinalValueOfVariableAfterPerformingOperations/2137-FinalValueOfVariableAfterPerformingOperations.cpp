// Last updated: 6/12/2025, 8:27:41 PM
class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int count=0;
        for(int i=0;i<operations.size();i++)
        {
            
                if( operations[i]=="--X" or operations[i]=="X--")
                count--;
                else
                count ++;

            
        }
        return count;
    }
};