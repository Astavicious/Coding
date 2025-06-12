// Last updated: 6/12/2025, 8:28:01 PM
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i=0;
        vector<int>x;
        vector<int>y;
        while(i<nums.size())
        {
            if(nums[i]!=0)
            {
                x.push_back(nums[i]);
            }
            else{
            y.push_back(nums[i]);
            }
            i++;
        }
        
        nums.assign(x.begin(),x.end());
        nums.insert(nums.end(),y.begin(),y.end());
    }
};