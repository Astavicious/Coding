// Last updated: 6/12/2025, 8:27:45 PM
class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> x;
        for(auto i : nums){x.push_back(i);}
        for(auto i : nums){ x.push_back(i);}
        return x;        
    }
};