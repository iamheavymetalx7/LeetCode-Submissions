class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        
        dp=[[[0 for k in range(3)] for j in range(2)]for i in range(n+1)]
## basce case starts----->
        for index in range(n+1):
            for buy in range(2):
                dp[index][buy][0]=0
        
        for buy in range(2):
            for cap in range(3):
                dp[n][buy][cap]=0
## it doesnt matter if we dont write base code, since all values are assigned to 0 in dp table   <----- base case ends
        
        
        for index in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(1,3): # since for cap==0, by the base case we have the value is always 0
                    
                    if buy:
                        dp[index][buy][cap] = max(-prices[index]+dp[index+1][0][cap],0+dp[index+1][1][cap])
                    else:
                        dp[index][buy][cap] = max(prices[index]+dp[index+1][1][cap-1],0 +dp[index+1][0][cap])

            
            
        return dp[0][1][2]
        
        
        
        
        
'''
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
'''
        