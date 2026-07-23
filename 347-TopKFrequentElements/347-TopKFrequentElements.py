# Last updated: 23/07/2026, 15:08:19
class Solution(object):
    def topKFrequent(self, nums, k):
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        sortdict = sorted(d,key=d.get,reverse=True)[:k]
        return sortdict

       

        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        