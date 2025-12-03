# Last updated: 12/3/2025, 1:08:18 AM
1class Solution(object):
2    def isAnagram(self, s, t):
3        if len(s)!=len(t):
4            return False
5        countS={}
6        countT={}
7        for i in range(len(s)):
8            countS[s[i]]=countS.get(s[i],0)+1
9            countT[t[i]]=countT.get(t[i],0)+1
10        return countS==countT
11
12        