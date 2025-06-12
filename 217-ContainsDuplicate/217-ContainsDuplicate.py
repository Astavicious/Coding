# Last updated: 6/12/2025, 8:28:12 PM
class Solution(object):
    def containsDuplicate(self, nums):
        lst=list()
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i] ==nums[i+1]:
                return True
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        