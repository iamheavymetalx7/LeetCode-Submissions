class Solution:
    def uniquePathsWithObstacles(self, oG: List[List[int]]) -> int:
        
        n,m=len(oG),len(oG[0])
        
        @cache
        def recur(i,j):
            
            if i<0 or j<0 or i>=n or j>=m or oG[i][j]==1:
                return 0
            if i==n-1 and j==m-1:
                return 1
            
            ans = 0
            ans= ans+recur(i+1,j)+recur(i,j+1)
            return ans
        
        val = recur(0,0)
        return val