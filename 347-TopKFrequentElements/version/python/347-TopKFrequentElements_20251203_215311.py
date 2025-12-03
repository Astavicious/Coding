# Last updated: 12/3/2025, 9:53:11 PM
1class Solution(object):
2    def topKFrequent(self, nums, k):
3        d=defaultdict(int)
4        for i in nums:
5            d[i]+=1
6        sortdict = sorted(d,key=d.get,reverse=True)[:k]
7        return sortdict
8
9       
10
11        """
12        :type nums: List[int]
13        :type k: int
14        :rtype: List[int]
15        """
16        