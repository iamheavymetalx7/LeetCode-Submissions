class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n=len(coins)
        dp=[[-1]*(amount+1) for _ in range(n)]
        
        
        def f(idx,amt):
            if idx==0:
                if amt%coins[idx]==0:
                    return 1
                else:
                    return 0
            if dp[idx][amt]!=-1:
                return dp[idx][amt]
            
            nottake = f(idx-1,amt)
            take = 0
            if coins[idx]<=amt:
                take = f(idx,amt-coins[idx])
            
            dp[idx][amt]=take+nottake
            return dp[idx][amt]
        return f(n-1,amount)