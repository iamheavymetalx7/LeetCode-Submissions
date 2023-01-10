class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        dp=[[-1]*2 for j in range(n+1)]
        
        
        def recur(index, buy):
            
            if index>=n:
                return 0
            
            if dp[index][buy]!=-1:
                return dp[index][buy]
            
            if buy:
                dp[index][buy]= max(-prices[index]+recur(index+1,0),0+recur(index+1,1))
                return dp[index][buy]
            else:
                dp[index][buy]=max(prices[index]-fee+recur(index+1,1),0+recur(index+1,0))
                return dp[index][buy]
        return recur(0,1)