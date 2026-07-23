# Last updated: 23/07/2026, 15:08:27
class Solution(object):
    def maxProfit(self, prices):
        i=0
        r=len(prices)
        profit=0
        mini=999999
        while i<r:           
            profit=max(profit,prices[i]-mini)
            mini=min(mini,prices[i])
            i+=1
            
            
           
        return profit

            
        """
        :type prices: List[int]
        :rtype: int
        """
        