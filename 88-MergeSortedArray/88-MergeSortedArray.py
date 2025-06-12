# Last updated: 6/12/2025, 8:28:13 PM
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        lst=list()
        for i in range(m,m+n):
            nums1[i]=nums2[i-m]
        nums1.sort()
        return nums1

        