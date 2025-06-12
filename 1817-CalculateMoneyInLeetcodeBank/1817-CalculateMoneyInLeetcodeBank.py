# Last updated: 6/12/2025, 8:27:46 PM
class Solution(object):
    def totalMoney(self, n):
        n=float(n)
        y=0
        if n>7:
            x= math.floor(n/7)
            z=n%7
            p=x
        
            for i in range (1,int(x+1)):
                m=i*1
                
                for j in range (7):
                    y+=m+j
            if z !=0:
                for k in range (1,int(z+1)):
                    p+=1
                    y+=p
                   
        else:
            for l in range (int(n)):
                r=l+1
                y+=r
        return int(y)