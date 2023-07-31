class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        
        n=len(s1)
        m =len(s2)
        
        dp = [[-1]*(m) for _ in range(n)]
        
        def recur(i,j):
            if i<0 or j<0:
                return 0

            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            if s1[i]==s2[j]:
                dp[i][j] = ord(s1[i])+recur(i-1,j-1)
                return dp[i][j]
            else:
                dp[i][j]=max(recur(i,j-1),recur(i-1,j))
                return dp[i][j]
        ans = recur(n-1,m-1)
        
        total = 0
        
        for i in range(n):     
            total += ord(s1[i])
        
        for j in range(m):
            total += ord(s2[j])
        
        
        return (total - 2*(ans))
        
            
            