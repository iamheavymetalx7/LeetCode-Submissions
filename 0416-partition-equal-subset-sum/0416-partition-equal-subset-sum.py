class Solution:
    def canPartition(self, a: List[int]) -> bool:
        
        summ=sum(a)
        length = len(a)
        if length==1:
            return False
        if summ%2:
            return False
        
        n=len(a)
        reqd = summ//2
        
        dp=[[0]*(reqd+1) for _ in range(n)]
        
        for i in range(n):
            dp[i][0]=True
        if a[0]<=reqd:
            dp[0][a[0]] = True
        
        for i in range(1,n):
            for target in range(1,reqd+1):
                
                nottake = dp[i-1][target]
                take = False
                if a[i]<=target:
                    take = dp[i-1][target-a[i]]
                
                dp[i][target] = take or nottake
        return dp[-1][-1]