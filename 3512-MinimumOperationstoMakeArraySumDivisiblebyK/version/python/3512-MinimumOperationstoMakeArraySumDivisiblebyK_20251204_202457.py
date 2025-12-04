# Last updated: 12/4/2025, 8:24:57 PM
1class Solution(object):
2    def minOperations(self, nums, k):
3        sumi=0
4        
5        for i in nums:
6            sumi+=i
7        return sumi%k
8        """
9        :type nums: List[int]
10        :type k: int
11        :rtype: int
12        """
13        