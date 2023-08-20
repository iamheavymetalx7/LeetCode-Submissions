class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        
       
        a=[[] for _ in range(n)]
        dp = [-1 for _ in range(n)] 
        
        for i in offers:
            a[i[0]].append(i)
            
        # print(a)
        
        def recur(idx):
            if idx>=n:
                return 0
            if dp[idx]!=-1:
                return dp[idx]
        
            ans = recur(idx+1)
            for buyers in a[idx]:
                ans = max(ans, buyers[2]+recur(buyers[1]+1))
            dp[idx]=ans
            return dp[idx]
        
        val = recur(0)
        
        return val
            