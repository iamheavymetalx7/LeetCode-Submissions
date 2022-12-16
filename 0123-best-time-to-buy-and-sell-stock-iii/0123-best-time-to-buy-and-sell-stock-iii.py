class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cap=2
        n=len(prices)
        
        dp=[[[-1]*3 for j in range(2)]for i in range(len(prices))]
        
        def recur(index,buy,cap):
            if cap<=0:
                return 0
            if index>=n:
                return 0
            if dp[index][buy][cap]!=-1:
                return dp[index][buy][cap]
            if buy:
                dp[index][buy][cap] = max(-prices[index]+recur(index+1,0,cap),0+recur(index+1,1,cap))
                return dp[index][buy][cap]
            else:
                dp[index][buy][cap] = max(prices[index]+recur(index+1,1,cap-1),0 +recur(index+1,0,cap))
                return dp[index][buy][cap]
            
        return recur(0,1,2)