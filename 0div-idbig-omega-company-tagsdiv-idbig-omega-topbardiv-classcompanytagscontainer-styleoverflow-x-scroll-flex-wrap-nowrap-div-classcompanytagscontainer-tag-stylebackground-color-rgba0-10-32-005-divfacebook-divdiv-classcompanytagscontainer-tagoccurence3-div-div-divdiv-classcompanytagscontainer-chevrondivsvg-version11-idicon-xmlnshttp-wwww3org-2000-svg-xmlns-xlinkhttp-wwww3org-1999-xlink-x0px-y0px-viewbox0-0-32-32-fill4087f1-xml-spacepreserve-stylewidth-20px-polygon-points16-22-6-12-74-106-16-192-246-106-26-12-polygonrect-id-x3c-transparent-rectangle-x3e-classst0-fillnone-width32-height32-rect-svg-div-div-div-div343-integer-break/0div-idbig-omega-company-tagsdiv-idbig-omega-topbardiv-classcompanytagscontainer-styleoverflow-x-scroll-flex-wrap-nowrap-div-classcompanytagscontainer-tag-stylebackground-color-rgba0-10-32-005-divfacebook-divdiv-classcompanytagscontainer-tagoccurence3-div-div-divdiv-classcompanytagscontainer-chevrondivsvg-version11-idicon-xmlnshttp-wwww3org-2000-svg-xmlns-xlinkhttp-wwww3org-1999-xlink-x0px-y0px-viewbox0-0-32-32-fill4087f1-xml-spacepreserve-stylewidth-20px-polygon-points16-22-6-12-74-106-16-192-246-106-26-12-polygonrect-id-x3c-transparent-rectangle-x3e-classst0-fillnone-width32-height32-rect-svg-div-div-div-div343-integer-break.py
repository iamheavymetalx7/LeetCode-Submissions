class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        
        @cache
        def recur(n):
            if n<0:
                return 0
            if n==0:
                return 1
            if n==2:
                return 2
            
            if n==3:
                return 3
            if n==4:
                return 4
            
            pdt=1
            pdt=max(2*recur(n-2),3*recur(n-3))
            return pdt
        ans = recur(n)

        return ans
        
        
            
            
        