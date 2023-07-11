class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n=len(coins)
        coins.sort()
        maxi =10**9
        dp=[[0]*(amount+1) for _ in range(n)]
        
        
        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i]= i//coins[0]
            else:
                dp[0][i]=10**9
        
        
        for i in range(1,n):
            for amt in range(0,amount+1):
                
                notpick =dp[i-1][amt]
                
                pick=10**9
                 
                if coins[i]<=amt:
                    pick =1+dp[i][amt-coins[i]]
                
                dp[i][amt]=min(pick, notpick)
        
        ans = dp[n-1][amount]
        
        if ans>=maxi:
            return -1
        return ans
            
        
        
#         def f(index,amount):
            
#             if index==0:
#                 if amount % coins[index]==0:
#                     return amount//coins[0]
#                 else:
#                     return 10**9
            
#             if dp[index][amount]!=-1:
#                 return dp[index][amount]
            
#             notpick = f(index-1,amount)
#             pick=10**9
            
#             if coins[index]<=amount:
#                 pick = 1+f(index, amount-coins[index])
            
#             dp[index][amount]=min(pick,notpick)
        
#             return dp[index][amount]
#         ans = f(n-1,amount)
        
#         if ans<maxi:
#             return ans
#         return -1
            
            