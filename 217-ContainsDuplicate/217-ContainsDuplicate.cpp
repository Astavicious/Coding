// Last updated: 6/12/2025, 8:28:07 PM
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int>check;
        for(int i=0;i<nums.size();i++)
        {
            if(check.find(nums[i])!=check.end())
            {
                return true;
            }
            check.insert(nums[i]);
        }
        return false;
    }
};