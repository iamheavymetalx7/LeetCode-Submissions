class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        
        n=len(prices)
        for i in range(n-1):
            maxProfit = max(0, prices[i+1]-prices[i])
            ans+=maxProfit
            
        return ans
'''
        
        def recur(index,buy):
            if index==n:
                return 0
            if dp[index][buy]!=-1:
                return dp[index][buy]
            if buy:
                dp[index][buy] = max(-prices[index]+recur(index+1,0),0+recur(index+1,1))
                return dp[index][buy]
            else:
                dp[index][buy] = max(prices[index]+recur(index+1,1), 0+recur(index+1,0))
                return dp[index][buy]
        return recur(0,1)
        
'''