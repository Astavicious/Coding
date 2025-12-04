# Last updated: 12/4/2025, 8:24:12 PM
1class Solution(object):
2    def minOperations(self, nums, k):
3        sum=0
4        
5        for i in nums:
6            sum+=i
7        return sum%k
8        """
9        :type nums: List[int]
10        :type k: int
11        :rtype: int
12        """
13        