# Last updated: 24/07/2026, 14:15:26

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums=nums1+nums2
        nums.sort()
        l=len(nums)
        if  l%2==0:
            x1=nums[int(l/2-1)]
            x2=nums[int(l/2)]
            res=(x1+x2)/2.0
        else:
            res=nums[int(l/2)]
        return res
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        