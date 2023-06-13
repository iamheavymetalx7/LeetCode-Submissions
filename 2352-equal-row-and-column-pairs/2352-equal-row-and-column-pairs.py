class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n =len(grid)
        m=len(grid[0])
        ans=[]
        
        
        for i in range(m):
            a=[]
            for j in range(n):
                a.append(grid[j][i])
            ans.append(a)
        cnt=0
        for row in grid:
            for col in ans:
                if row == col:
                    cnt+=1
        
        return cnt