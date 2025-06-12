// Last updated: 6/12/2025, 8:28:06 PM
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int,int>occur;
        for(int i=0;i<nums.size();i++)
        {
            if(occur.find(nums[i])!=occur.end())
            {
                occur[nums[i]]++;
            }
            else
            {
                occur[nums[i]]=1;
            }
        }
        int max=0;
        int val=0;
       for(auto i=occur.begin();i!=occur.end();i++)
       {
        if(i->second>max)
        {
            max=i->second;
            val=i->first;
        }
       }
       return val;
        
    }
};