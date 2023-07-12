class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        
        n,m=len(w1),len(w2)
        
        dp=[[-1]*(m+1) for _ in range(n+1)]
        
        
        def f(i,j):
            if i<0: return j+1
            if j<0: return i+1
                
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            if w1[i]==w2[j]:
                dp[i][j] = f(i-1,j-1)
            else:
                dp[i][j] = 1+ min(f(i-1,j-1),f(i,j-1),f(i-1,j))
            
            return dp[i][j]
        
        return f(n-1,m-1)