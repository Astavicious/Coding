# Last updated: 12/1/2025, 8:18:00 PM
1class Solution(object):
2    def isAnagram(self, s, t):
3        if len(s)!=len(t):
4            return False
5        return sorted(s)==sorted(t)
6        