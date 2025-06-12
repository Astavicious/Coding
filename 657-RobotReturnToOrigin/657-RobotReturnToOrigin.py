# Last updated: 6/12/2025, 8:27:57 PM
class Solution(object):
    def judgeCircle(self, moves):
      count=0
      dct={  "U":2,"D":-2,"R":3,"L":-3}
      for i in range(len(moves)):
          count+=dct[moves[i]]
      if count==0:return True
      else: return False
        