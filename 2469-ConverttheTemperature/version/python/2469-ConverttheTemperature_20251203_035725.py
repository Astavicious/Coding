# Last updated: 12/3/2025, 3:57:25 AM
1class Solution(object):
2    def convertTemperature(self, celsius):
3        return [celsius+ 273.15,celsius * 1.80 + 32.00]
4        """
5        :type celsius: float
6        :rtype: List[float]
7        """
8        