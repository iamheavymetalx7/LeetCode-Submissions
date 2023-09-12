class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n=len(matrix);m=len(matrix[0])
        dire =[(1,0),(0,1),(-1,0),(0,-1)]
        
        @lru_cache(None)
        def dfs(i,j):
            ans =1
            for dx,dy in dire:
                dx+=i
                dy+=j
                if 0<=dx<n and 0<=dy<m and matrix[dx][dy]>matrix[i][j]:
                    ans=max(ans,1+dfs(dx,dy))
            return ans
        
        ans = 0
        for i in range(n):
            for j in range(m):
                ans =max(ans,dfs(i,j))
        return ans
 