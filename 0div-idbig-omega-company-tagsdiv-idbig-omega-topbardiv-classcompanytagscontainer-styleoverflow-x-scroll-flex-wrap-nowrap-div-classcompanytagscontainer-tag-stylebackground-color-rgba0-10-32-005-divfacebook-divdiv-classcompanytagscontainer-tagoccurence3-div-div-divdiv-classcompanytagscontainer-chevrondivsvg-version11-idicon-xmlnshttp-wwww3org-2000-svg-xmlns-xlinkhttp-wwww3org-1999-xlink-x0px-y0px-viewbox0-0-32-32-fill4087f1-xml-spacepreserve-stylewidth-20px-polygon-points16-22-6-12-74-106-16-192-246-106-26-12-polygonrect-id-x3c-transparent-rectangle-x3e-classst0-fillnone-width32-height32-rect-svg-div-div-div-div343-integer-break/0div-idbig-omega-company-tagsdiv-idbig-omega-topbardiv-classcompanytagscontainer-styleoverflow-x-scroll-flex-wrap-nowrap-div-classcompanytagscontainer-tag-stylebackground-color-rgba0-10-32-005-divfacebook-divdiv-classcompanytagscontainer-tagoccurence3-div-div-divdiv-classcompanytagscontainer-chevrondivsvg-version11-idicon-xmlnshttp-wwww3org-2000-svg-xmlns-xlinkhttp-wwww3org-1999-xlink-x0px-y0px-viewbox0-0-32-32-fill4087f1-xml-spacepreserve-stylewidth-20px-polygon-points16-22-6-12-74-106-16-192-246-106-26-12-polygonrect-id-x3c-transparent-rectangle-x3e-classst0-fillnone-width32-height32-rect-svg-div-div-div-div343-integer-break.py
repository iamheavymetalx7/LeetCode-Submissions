class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        


        @cache
        def recur(idx):
            if idx<0:
                return 0
            if idx==0:
                return 1
            ans=1
            for j in range(2,5):
                if idx-j>=0:
                    ans = max(ans,j*recur(idx-j))
            return ans

        val = recur(n)
        return val
        
        
            
            
        