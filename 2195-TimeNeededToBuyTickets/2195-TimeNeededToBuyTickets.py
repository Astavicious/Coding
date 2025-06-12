# Last updated: 6/12/2025, 8:27:40 PM
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        count = 0
        while tickets[k] > 0:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    count += 1
                    if i == k and tickets[i] == 0:  
                        break

        return count
        

        

        