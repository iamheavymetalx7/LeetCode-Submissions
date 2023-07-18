class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1]*(n)

        def recur(idx):

            if idx>=n:return 0

            if dp[idx]!=-1:
                return dp[idx]

            ans= cost[idx]+min(recur(idx+1),recur(idx+2))

            dp[idx]= ans

            return dp[idx]
        
        ans = recur(0)
        an2 = recur(1)
        return min(ans,an2)
    

        