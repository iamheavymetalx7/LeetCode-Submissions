class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp=[-1]*(n+10)
        dp[0]=0
        dp[1]=1
        dp[2]=2
        
        # print(dp)
    
    
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        # print(dp)
        return dp[n]
        