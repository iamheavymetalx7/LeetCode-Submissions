class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        a=[[] for _ in range(n)]
        
        for i in range(len(offers)):
            a[offers[i][0]].append(i)
        
        dp =[-1 for _ in range(n+1)]
        def recur(idx):
            if idx>=n:
                return 0
            
            if dp[idx]!=-1:
                return dp[idx]
            
            ans =0
            ans = max(ans, recur(idx+1))
            
            for ele in a[idx]:
                ans = max(ans,offers[ele][2]+recur(offers[ele][1]+1))
            
            dp[idx]=ans
            return dp[idx]
        
        val = recur(0)
        return val