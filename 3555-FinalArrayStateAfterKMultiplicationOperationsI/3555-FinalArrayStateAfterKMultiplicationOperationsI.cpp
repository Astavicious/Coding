// Last updated: 6/12/2025, 8:27:43 PM
class Solution {
public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        int r=k;
        while(r>0)
        {
            int x=*min_element(nums.begin(),nums.end());
            auto it=find(nums.begin(),nums.end(),x);
            *it=x*multiplier;
            r--;
        }
        return nums;
            }
};