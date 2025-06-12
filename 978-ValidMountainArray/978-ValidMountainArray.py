# Last updated: 6/12/2025, 8:27:55 PM
class Solution(object):
    def validMountainArray(self, arr):
        j=0
        if len(arr)<3:
            return False
        for i in range(len(arr)-1):
            if arr[i]>arr[j]:
                j=i
        if j==0:
            return False
        for i in range(j-1):
            if arr[i]>=arr[i+1]:
                return False
        for i in range(j,len(arr)-1):
            if arr[i]<=arr[i+1]:
                return False
        else:
            return True
        
        
            

        """
        :type arr: List[int]
        :rtype: bool
        """
        