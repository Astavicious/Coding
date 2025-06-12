# Last updated: 6/12/2025, 8:28:02 PM
class Solution(object):
    def missingNumber(self, nums):
        l=sum(nums)
        r=len(nums)
        res=r*(r+1)/2
        return res-l

        