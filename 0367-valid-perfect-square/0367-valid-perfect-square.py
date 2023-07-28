class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        l=-1
        r = int(1e18)
        
        while r-l>1:
            m =(l+r)//2
            if m**2 >num:
                r=m
            else:
                l=m
        
        if l**2 == num:
            return True
        
        return False