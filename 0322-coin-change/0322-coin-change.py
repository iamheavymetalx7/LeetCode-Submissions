class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n=len(coins)
        coins.sort()
        maxi =10**9
        dp=[[-1]*(amount+1) for _ in range(n)]
        
        
        def f(index,amount):
            
            if index==0:
                if amount % coins[index]==0:
                    return amount//coins[0]
                else:
                    return 10**9
            
            if dp[index][amount]!=-1:
                return dp[index][amount]
            
            notpick = f(index-1,amount)
            pick=10**9
            
            if coins[index]<=amount:
                pick = 1+f(index, amount-coins[index])
            
            dp[index][amount]=min(pick,notpick)
        
            return dp[index][amount]
        ans = f(n-1,amount)
        
        if ans<maxi:
            return ans
        return -1
            
            