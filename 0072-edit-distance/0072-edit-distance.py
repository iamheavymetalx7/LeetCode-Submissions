class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        
        dp = [[-1]*(m+1) for i in range(n+1)]
        
        def recur(i,j):
            if i==0:
                return j
            if j==0:
                return i
            if dp[i][j]!=-1:
                return dp[i][j]
            
            if word1[i-1]==word2[j-1]:
                dp[i][j] = 0 + recur(i-1,j-1)
            else:
                dp[i][j] = 1+ min(recur(i-1,j-1),recur(i-1,j),recur(i,j-1))
            return dp[i][j]
        return recur(n,m)
                