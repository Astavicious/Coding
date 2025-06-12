# Last updated: 6/12/2025, 8:27:50 PM
class Solution(object):
    def runningSum(self, nums):
        for i in range(len(nums)):
            if i>0:
                nums[i]=nums[i-1]+nums[i]
        return nums
            






        """
        :type nums: List[int]
        :rtype: List[int]
        """