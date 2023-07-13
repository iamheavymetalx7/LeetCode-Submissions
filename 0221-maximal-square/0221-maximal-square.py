class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n=len(matrix); m=len(matrix[0])
        dp=[[0]*(m) for _ in range(n)]
            
        maxi=0
        for i in range(n):
            if matrix[i][0]=="1":
                dp[i][0] = 1
                maxi=max(maxi, dp[i][0])
        
        for j in range(m):
            if matrix[0][j]=="1":
                dp[0][j] = 1
                maxi=max(maxi, dp[0][j])

        
        
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]=="1":
                    dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
                    maxi=max(maxi, dp[i][j])
        
        return maxi**2
                