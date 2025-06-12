# Last updated: 6/12/2025, 8:28:03 PM
class Solution(object):
    def isAnagram(self, s, t):
        if(sorted(s)==sorted(t)):
            return True
        return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        