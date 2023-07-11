class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n)]
        
        
        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i]=1
            
        
        for i in range(1,n):
            for amt in range(amount+1):
                take =0
                
                nottake = dp[i-1][amt]
                if coins[i]<=amt:
                    take = dp[i][amt-coins[i]]
                
                
                dp[i][amt] = take+nottake
        return dp[n-1][amount]
        
                                 
        
#         def f(idx,amt):
#             if idx==0:
#                 if amt%coins[idx]==0:
#                     return 1
#                 else:
#                     return 0
#             if dp[idx][amt]!=-1:
#                 return dp[idx][amt]
            
#             nottake = f(idx-1,amt)
#             take = 0
#             if coins[idx]<=amt:
#                 take = f(idx,amt-coins[idx])
            
#             dp[idx][amt]=take+nottake
#             return dp[idx][amt]
        # return f(n-1,amount)