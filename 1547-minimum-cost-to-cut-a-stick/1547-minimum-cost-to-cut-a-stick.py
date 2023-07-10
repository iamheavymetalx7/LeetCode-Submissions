class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        c=len(cuts)

        cuts.insert(0,0)
        cuts.append(n)
        cuts.sort()
        
        dp=[[-1]*(c+1) for _ in range(c+1)]
        
        
        def f(i,j):
            if i>j:
                return 0
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            res=10**9
            
            for ind in range(i,j+1):
                cost = cuts[j+1] - cuts[i-1] + f(i,ind-1)+f(ind+1,j)
                res=min(res,cost)
            
            dp[i][j]=res
            return dp[i][j]
            
        
        return f(1,c)