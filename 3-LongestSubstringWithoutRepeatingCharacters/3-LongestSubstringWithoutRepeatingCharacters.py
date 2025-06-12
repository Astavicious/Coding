# Last updated: 6/12/2025, 8:28:27 PM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        lst=list()
        res=0
        r=len(s)
        for i in range(r):
            if s[i] not in lst:
                lst.append(s[i])
                continue
            elif s[i] in lst:
                res=max(res,len(lst))
                while s[i] in lst:
                    lst.pop(0)
                lst.append(s[i])
                
        res=max(res,len(lst))
        return res
            
            
        
            
    

            

            

        """
        :type s: str
        :rtype: int
        """
        