# Last updated: 6/12/2025, 8:27:49 PM
class Solution(object):
    def maximumWealth(self, accounts):
      res=0
      for i in range(len(accounts)):
        res=max(sum(accounts[i]),res)
      return res




        