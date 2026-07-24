# Last updated: 24/07/2026, 14:15:53
1
2class Solution(object):
3    def findMedianSortedArrays(self, nums1, nums2):
4        nums=nums1+nums2
5        nums.sort()
6        l=len(nums)
7        if  l%2==0:
8            x1=nums[int(l/2-1)]
9            x2=nums[int(l/2)]
10            res=(x1+x2)/2.0
11        else:
12            res=nums[int(l/2)]
13        return res
14        """
15        :type nums1: List[int]
16        :type nums2: List[int]
17        :rtype: float
18        """
19        