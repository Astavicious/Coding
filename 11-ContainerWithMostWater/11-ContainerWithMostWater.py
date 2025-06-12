# Last updated: 6/12/2025, 8:28:24 PM
class Solution(object):
    def maxArea(self, height):
        area=0
        l=0
        r=len(height)-1
        while(l<r):
            area=max(area,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return area
        

            
        """
        :type height: List[int]
        :rtype: int
        """
        