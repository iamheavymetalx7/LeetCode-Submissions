class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        dp=[[-1]*2 for _ in range(n+1)]
        
        def recur(idx,buy):
            if idx>=n:
                return 0
            
            if dp[idx][buy]!=-1:
                return dp[idx][buy]
                
            
            if buy:
                take = recur(idx+1,0)-prices[idx]
                nottake = recur(idx+1,1)
                
                dp[idx][buy] = max(take,nottake)
                return dp[idx][buy]
            else:
                take = recur(idx+1, 1)+prices[idx]-fee
                nottake = recur(idx+1,0)
                dp[idx][buy]= max(take,nottake)
                
                return dp[idx][buy]
            
        return recur(0,1)
                
        