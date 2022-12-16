##Tabulation of recursive/memoized code
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        
        dp=[[0]*2 for j in range(len(prices)+1)]
        
        for j in range(2):
            dp[n][j]=0
        # we start from reverse when compared to recursive code 
        for index in range(n-1,-1,-1) :
            for buy in range(2):
                if buy:
                    dp[index][buy] = max(-prices[index]+dp[index+1][0],0+dp[index+1][1])
                else:
                    dp[index][buy] = max(prices[index]+dp[index+1][1], 0+dp[index+1][0])
                                        
        return dp[0][1]      
'''
        ## recursive code:
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
        
        
        ## pretty easier solution based on observation:
            def maxProfit(self, prices: List[int]) -> int:
        ans=0
        
        n=len(prices)
        for i in range(n-1):
            maxProfit = max(0, prices[i+1]-prices[i])
            ans+=maxProfit
            
        return ans
        
        
        
'''