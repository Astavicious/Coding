# Last updated: 6/12/2025, 8:28:05 PM
class Solution(object):
    def moveZeroes(self, nums):
        j=0
        for num in nums:
            if num!=0:
                nums[j]=num
                j+=1
        for i in range(j,len(nums)):
            nums[i]=0
            
                
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        