import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[[-1 for i in range(amount+1)] for j in range(len(coins))]
        
        
        def recur(index,amount):
            if index==0:
                if amount % coins[index]==0:
                    return amount//coins[index]
                else:
                    return math.inf
            if dp[index][amount]!=-1:
                return dp[index][amount]
            nottake = recur(index-1,amount)
            take=math.inf
            if coins[index]<=amount:
                take=1+recur(index,amount-coins[index])
            
            dp[index][amount]  = min(take,nottake)
            return dp[index][amount]
        ans =  recur(len(coins)-1,amount)
        return ans if ans!=math.inf else -1