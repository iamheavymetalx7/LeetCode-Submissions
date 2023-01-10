class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1]*2 for j in range(n)]

        def recur(index,buy):
            if index>=n:
                return 0
            if dp[index][buy]!=-1:
                return dp[index][buy]
            if buy:
                dp[index][buy]  = max(-prices[index]+recur(index+1,0),0+recur(index+1,1))
                return dp[index][buy]
            else: ## sell
                dp[index][buy]= max(prices[index]+recur(index+2,1), recur(index+1,0))
                return dp[index][buy]
        return recur(0,1)
    
    

    
#     def recur_maxProfit(self, prices: List[int]) -> int:
        
#         n=len(prices)
#         def recur(index,buy):
#             if index>=n:
#                 return 0
            
#             if buy:
#                 return max(-prices[index]+recur(index+1,0),0+recur(index+1,1))
#             else: ## sell
#                 return max(prices[index]+recur(index+2,1), recur(index+1,0))
        
#         return recur(0,1)