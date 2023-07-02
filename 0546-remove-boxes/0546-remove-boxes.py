class Solution:
    def removeBoxes(self, b: List[int]) -> int:
        
        n=len(b)
        
        @cache
        def dp(l,r,k):
            if l>r:
                return 0
            while l+1<=r and b[l]==b[l+1]:
                l+=1
                k+=1
            ans = 0
            ans = (k+1)*(k+1)+ dp(l+1,r,0)
            
            for m in range(l+1,r+1):
                if b[l]==b[m]:
                    ans=max(ans, dp(m,r,k+1)+dp(l+1,m-1,0))
            
            return ans
        return dp(0,n-1,0)