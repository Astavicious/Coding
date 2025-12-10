# Last updated: 12/10/2025, 1:25:22 AM
1class Solution(object):
2    def maxProfit(self, prices):
3        i=0
4        r=len(prices)
5        profit=0
6        mini=999999
7        while i<r:
8            mini=min(mini,prices[i])
9            profit=max(profit,prices[i]-mini)
10            i+=1
11            
12            
13           
14        return profit
15
16            
17        """
18        :type prices: List[int]
19        :rtype: int
20        """
21        