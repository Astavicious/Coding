# Last updated: 12/8/2025, 3:02:17 PM
1class Solution(object):
2    def isPalindrome(self, s):
3        l=0
4        r=len(s)-1
5        while l<r:
6            if (l<r) and not (s[l].isalnum()):
7                l+=1
8                continue
9            if l<r and not (s[r].isalnum()):
10                r-=1
11                continue
12            if s[l].lower()!= s[r].lower():
13                return False
14            l+=1
15            r-=1
16        return True
17
18        """
19        :type s: str      
20        :rtype: bool
21        """
22        