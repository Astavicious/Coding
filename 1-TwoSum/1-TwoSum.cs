// Last updated: 6/12/2025, 8:28:30 PM
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int x=0;
        int[] dummy=new int[2];
        for (int i=0;i<nums.Length;i++)
        {
            x=nums[i];
            
            for(int j=i+1;j<nums.Length;j++)
            {
                if(nums[j]==target-x)
                {
                    dummy[0]=i;
                    dummy[1]=j;
                    break;
                }
            }
        }
        return dummy;
        
    }
}