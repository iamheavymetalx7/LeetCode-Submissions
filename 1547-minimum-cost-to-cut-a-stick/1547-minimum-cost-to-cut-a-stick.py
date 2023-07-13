class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        c=len(cuts)
        
        
        cuts=[0]+cuts+[n]
        cuts.sort()
        
        
        dp=[[-1]*(c+1) for _ in range(c+1)]
        
        def f(i,j):
            if i>j:
                return 0
            
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            
            mini = 10**9
            for k in range(i,j+1):
                ans = cuts[j+1]-cuts[i-1]+f(i,k-1)+f(k+1,j)
                mini = min(ans, mini)
            
            dp[i][j] =mini
            return dp[i][j]
        return f(1,c)