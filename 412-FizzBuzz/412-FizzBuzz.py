# Last updated: 6/12/2025, 8:27:59 PM
class Solution(object):
    def fizzBuzz(self, n):
        lst=list()
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                lst.append( "FizzBuzz")
            elif i%3==0 and i%5!=0:
                lst.append( "Fizz")
            elif i%5==0 and i%3!=0:
                lst.append( "Buzz")
            else:
                
                lst.append(str(i))
        return lst
    
        