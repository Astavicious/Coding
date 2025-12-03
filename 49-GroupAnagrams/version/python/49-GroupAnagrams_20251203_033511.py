# Last updated: 12/3/2025, 3:35:11 AM
1
2
3class Solution(object):
4    def groupAnagrams(self, strs):
5        out= defaultdict(list)
6        
7        for i in strs:
8            count=[0]*26
9            for j in i:
10                x=ord(j)-ord('a')
11                count[x]+=1
12            key=tuple(count)
13            out[key].append(i)
14        return out.values()
15
16        """
17        :type strs: List[str]
18        :rtype: List[List[str]]
19        """
20        