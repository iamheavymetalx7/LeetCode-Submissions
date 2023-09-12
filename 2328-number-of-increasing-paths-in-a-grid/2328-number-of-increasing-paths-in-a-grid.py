class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        n,m=len(grid),len(grid[0])
        MOD = int(1e9)+7
        dire = [(1,0),(0,1),(0,-1),(-1,0)]
        
        @lru_cache(None)
        def dfs(i,j):
            
            ans = 1
            for dx,dy in dire:
                dx+=i
                dy+=j
                if 0<=dx<n and 0<=dy<m and grid[dx][dy]>grid[i][j]:
                    ans=(ans+dfs(dx,dy))
                    ans%=MOD
                
            return ans
        ans=0
        for i in range(n):
            for j in range(m):
                ans+=dfs(i,j)
                ans%=MOD
        
        return ans