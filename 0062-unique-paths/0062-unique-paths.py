class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cnt =0
        
        dp = [[-1 for _ in range(n)] for _ in range(m)]    
    
        def recur(i,j):
            
            if i>=m or j>=n:
                return 0
    
            if i==m-1 and j==n-1:
                return 1
            
            if dp[i][j]!=-1:return dp[i][j]

            
   
            
                
            
            down = recur(i+1,j)
            right = recur(i,j+1)
            
            dp[i][j]= down+right
            
            return dp[i][j]
        
        return recur(0,0)