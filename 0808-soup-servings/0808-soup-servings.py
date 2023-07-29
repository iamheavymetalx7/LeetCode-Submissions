class Solution:
    def soupServings(self, n: int) -> float:
        
        # print(int(5e3))
        # dp =[[-1]*(int(5e3)) for _ in range(int(5e3))]
        
        @cache
        def recur(n,m):
            if n<=0 and m<=0:
                return 0.5
            elif n<=0:
                return 1
            elif m<=0:
                return 0
            
#             if dp[n][m]!=-1:
#                 return dp[n][m]
            
                
            
            
            ans =0
            ans+=0.25*recur(n-100,m)
            ans+=0.25*recur(n-75,m-25)
            ans+=0.25*recur(n-50,m-50)
            ans+=0.25*recur(n-25,m-75)
            
            return ans
            
            return dp[n][m]
        
        if n>=int(5e3):
            return 1.0
        
        ret=recur(n,n)
        return (ret)