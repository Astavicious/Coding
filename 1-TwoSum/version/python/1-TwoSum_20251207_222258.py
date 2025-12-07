# Last updated: 12/7/2025, 10:22:58 PM
1class Solution(object):
2    def twoSum(self, nums, target):
3        d={}
4        for i in range(len(nums)):
5            if nums[i] in d:
6                return [d[nums[i]],i]
7            d[target-nums[i]]=i
8
9
10
11        
12            
13        """
14        :type nums: List[int]
15        :type target: int
16        :rtype: List[int]
17        """
18        