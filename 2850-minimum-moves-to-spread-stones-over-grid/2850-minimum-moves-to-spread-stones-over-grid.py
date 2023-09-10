class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        def solve(grid,s):
            # print(grid)
            ans = int(1e19)
            if s==0:
                return 0
            

            for i in range(3):
                for j in range(3):
                    if grid[i][j]==0:
                        for dx in range(3):
                            for dy in range(3):
                                if grid[dx][dy]>1:
                                    grid[dx][dy]-=1
                                    grid[i][j]+=1   
                                    ans = min(ans, abs(i-dx)+abs(j-dy)+solve(grid,s-1))
                                    grid[dx][dy]+=1
                                    grid[i][j]-=1
            return ans
        
        s= 0
        
        for i in range(3):
            for j in range(3):
                if grid[i][j]==0:
                    s+=1
        
        val = solve(grid,s)
        return val