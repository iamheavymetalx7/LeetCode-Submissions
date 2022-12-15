class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[[-1 for i in range(amount+1)] for j in range(len(coins))]
        
        def recur(index,amount):
            if index==0:
                if amount%coins[0]==0:
                    return 1
                return 0
            if dp[index][amount]!=-1:
                return dp[index][amount]
            nottake = recur(index-1,amount)
            take = 0
            if coins[index]<=amount:
                take = recur(index,amount-coins[index])
            
            dp[index][amount]=take+nottake
            
            return dp[index][amount]
        return recur(len(coins)-1,amount)