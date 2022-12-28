class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        dp=[[0]*(m+1) for j in range(n+1)]
        maxi=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if matrix[i-1][j-1]=="1":
                        dp[i][j]= 1 + min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
                
                        maxi=max(maxi,dp[i][j])
            
        print(dp)
        return maxi**2