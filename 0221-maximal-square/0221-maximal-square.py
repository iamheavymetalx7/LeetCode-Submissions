class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n=len(matrix); m=len(matrix[0])
        dp=[[0]*(m) for _ in range(n)]
        maxi=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=="1":
                    dp[i][j]=1
                    if i>0 and j>0:
                        dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                maxi=max(maxi,dp[i][j])
        
        
        return maxi**2