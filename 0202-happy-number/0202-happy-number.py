class Solution:
    def sqrd(self,n):
        return sum([int(x)**2 for x in str(n)])
    
    def isHappy(self, num: int) -> bool:
        slow=num
        fast=num
        
        while True:
            slow=self.sqrd(slow)
            fast=self.sqrd(self.sqrd(fast))
            
            if fast==slow:
                break
                
        return fast==1