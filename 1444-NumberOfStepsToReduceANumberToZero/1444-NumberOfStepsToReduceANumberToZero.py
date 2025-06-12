# Last updated: 6/12/2025, 8:27:53 PM
class Solution(object):
    def numberOfSteps(self, num):
        count=0
        while(num>=1):
            if (num%2==0):
                num=num/2
                count+=1
            else:
                num-=1
                count+=1
        return count



        """
        :type num: int
        :rtype: int
        """
        