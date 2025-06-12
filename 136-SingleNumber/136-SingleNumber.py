# Last updated: 6/12/2025, 8:28:09 PM
class Solution(object):
    def singleNumber(self, nums):
      nums.sort()
      i=1
      while(i<len(nums)):
        if nums[i]==nums[i-1]:
          i+=2
          continue
        else:
          return nums[i-1]
      return nums[len(nums)-1]
        