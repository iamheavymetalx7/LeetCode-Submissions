class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        dp=[[-1]*(m+1) for _ in range(n+1)]
        
        #if insert: i,j+1
        #if delete: i+1,j
        #if replace:i+1,j+1    
        
        def recur(i,j):
            if i>=n:
                return m-j
            if j>=m:
                return n-i
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            if word1[i]==word2[j]:
                dp[i][j] = 0+recur(i+1,j+1)
            else:
                dp[i][j]=1+min(recur(i+1,j+1),recur(i,j+1),recur(i+1,j))
            
            
            return dp[i][j]
        
        
        return recur(0,0)