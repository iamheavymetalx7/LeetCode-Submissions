class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        @cache
        def recur(l,r):
            if l>=r:
                return 0
            ans=int(1e19)
            
            for i in range(l,r+1):
                ans = min(ans,i+max(recur(l,i-1),recur(i+1,r)))
            return ans
        
        val = recur(1,n)
        return val
            