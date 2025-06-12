# Last updated: 6/12/2025, 8:27:51 PM
class Solution(object):
    def maxProduct(self, nums):
        lst=list()
        for i in nums:
            lst.append(i)
        x=max(lst)-1
        lst.remove(x+1)
        return x*(max(lst)-1)



        """
        :type nums: List[int]
        :rtype: int
        """
        