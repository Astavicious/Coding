# Last updated: 6/12/2025, 8:28:25 PM
class Solution(object):
    def isPalindrome(self, x):
        r=str(x)
        y=str(x)[::-1]
        if y == r:
            return True
        else:
          return False
        """
        :type x: int
        :rtype: bool
        """
        