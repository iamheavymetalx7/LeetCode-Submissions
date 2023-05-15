class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        ans=0
        mod=10**9+7
        dp=[0]*(high+1)
        
        dp[0]=1
        
        for i in range(1,high+1):
            dp[i] = ((dp[i-zero] if i-zero>=0 else 0) + (dp[i-one] if i-one>=0 else 0))%mod
            
            if i>=low:
                ans = ans+dp[i]
                ans = ans % mod
        return ans
                
        
        
        
        

        ## Recursive Code:
        
#         def recur(s,ans):
#             if len(s)>=low and len(s)<=high:
#                 ans+=[s]
            
#             if len(s)>high:
#                 return
            
#             recur(s+"0"*zero, ans)
#             recur(s+"1"*one, ans)
            
            
#             return
#         mod=10**9+7
#         s=""
#         ans=[]
        
#         recur(s,ans)
        
#         return len(ans)%mod
            
        