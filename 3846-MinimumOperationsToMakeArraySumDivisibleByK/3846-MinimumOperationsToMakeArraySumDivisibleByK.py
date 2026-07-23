# Last updated: 23/07/2026, 15:08:04
class Solution(object):
    def minOperations(self, nums, k):
        sumi=0
        
        for i in nums:
            sumi+=i
        return sumi%k
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        