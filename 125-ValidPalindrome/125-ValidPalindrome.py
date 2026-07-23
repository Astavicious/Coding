# Last updated: 23/07/2026, 15:08:25
class Solution(object):
    def isPalindrome(self, s):
        l=0
        r=len(s)-1
        while l<r:
            if (l<r) and not (s[l].isalnum()):
                l+=1
                continue
            if l<r and not (s[r].isalnum()):
                r-=1
                continue
            if s[l].lower()!= s[r].lower():
                return False
            l+=1
            r-=1
        return True

        """
        :type s: str      
        :rtype: bool
        """
        