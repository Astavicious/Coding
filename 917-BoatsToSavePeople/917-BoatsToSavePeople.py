# Last updated: 6/12/2025, 8:27:56 PM
class Solution(object):
    def numRescueBoats(self, people, limit):
        count = 0
        people.sort()
        left=0
        right=len(people)-1
        while(left<=right):
            if left==right:
                count+=1
                break
            elif(people[left]+people[right])<=limit:
                count+=1
                left+=1
                right-=1
                continue
            else:
                right-=1
                count+=1
        return count







        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        