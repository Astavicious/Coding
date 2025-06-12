// Last updated: 6/12/2025, 8:28:29 PM
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int diff{};
        vector<int> ret{};
        unordered_map<int,int> dict;
        for(int i=0;i<nums.size();i++)
        {   diff=target-nums[i];
            if(dict.find(diff)!=dict.end())//if not found maps return the last index
            {
                ret.push_back(i);
                ret.push_back(dict[diff]);
                return ret;
            }
            dict[nums[i]]=i;
        }
        return ret;
    }
};