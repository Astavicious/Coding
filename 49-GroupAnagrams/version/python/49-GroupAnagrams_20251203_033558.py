# Last updated: 12/3/2025, 3:35:58 AM
1
2
3class Solution(object):
4    def groupAnagrams(self, strs):
5        out= defaultdict(list)
6        for i in strs:
7            count=[0]*26
8            for j in i:
9                count[ord(j)-ord('a')]+=1
10            key=tuple(count)
11            out[key].append(i)
12        return out.values()
13
14        """
15        :type strs: List[str]
16        :rtype: List[List[str]]
17        """
18        