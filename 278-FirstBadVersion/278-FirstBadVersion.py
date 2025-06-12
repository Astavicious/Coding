# Last updated: 6/12/2025, 8:28:00 PM
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
class Solution(object):
    def firstBadVersion(self, n):
        
        first=0
        last=n
        while(first<last):
            mid=(first+last)/2
            if not isBadVersion(mid):
                first=mid+1
            else:
                last=mid
        return first




  
    
        