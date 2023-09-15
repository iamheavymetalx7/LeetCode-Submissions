class Solution:
    def arrangeCoins(self, n: int) -> int:
        l=0
        r=int(1e18)
        
        while r-l>1:
            mid =(l+r)//2
            
            if (mid*(mid+1))//2>n:
                r=mid
            else:
                l=mid
        return r-1