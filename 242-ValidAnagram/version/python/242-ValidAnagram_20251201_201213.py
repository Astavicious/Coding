# Last updated: 12/1/2025, 8:12:13 PM
1class Solution(object):
2    def isAnagram(self, s, t):
3        if len(s)!=len(t):return False
4        sim=sorted(s)
5        tim=sorted(t)
6        s=sim
7        t=tim
8        for i in range(len(s)):
9            if s[i]!=t[i]:
10                return False
11        return True
12        