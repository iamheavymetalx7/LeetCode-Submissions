class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[0 for j in range(k+1)]for x in range(2)]for i in range(n+1)]
        
        
## base case starts ---->>
## not writing any base cases since they are all covered as states in buy and sell stock3


##                          <<------- base case ends....
        
        for index in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(1,k+1):
                    if buy:
                        dp[index][buy][cap] = max(-prices[index]+dp[index+1][0][cap], dp[index+1][1][cap])
                        
                    else:
                        dp[index][buy][cap] = max( prices[index]+dp[index+1][1][cap-1], dp[index+1][0][cap])
                        
                        
        return dp[0][1][k]