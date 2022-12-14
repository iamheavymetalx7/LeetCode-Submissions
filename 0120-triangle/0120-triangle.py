class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        m=len(triangle[-1])
        
        dp=[[-1 for x in range(m)] for y in range(n)]
        
        def recur(i,j):
            if i==n-1:
                return triangle[n-1][j]
            if dp[i][j]!=-1:
                return dp[i][j]
            
            dir1=triangle[i][j]+recur(i+1,j)
            dir2=triangle[i][j]+recur(i+1,j+1)
            
            dp[i][j] = min(dir1,dir2)
            return dp[i][j]

        return recur(0,0)