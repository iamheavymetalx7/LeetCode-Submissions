class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        dire =[(-1,0),(1,0),(0,-1),(0,1),(1,1),(-1,-1),(1,-1),(-1,1)]
        n=len(grid)
        m=len(grid[0])
        q=deque()
        q.append([0,0,1])
        
        vis=set()
        ans=int(1e19)
        
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        
        while q:
            x,y,p = q.popleft()
            # print(x,y,p)
            vis.add((x,y))
            if x==n-1 and y==n-1:
                ans=min(ans,p)
            for dx,dy in dire:
                newx=x+dx
                newy=y+dy
                if 0<=newx<n and 0<=newy<m and (newx,newy) not in vis and grid[newx][newy]==0:
                    vis.add((newx,newy))
                    q.append([newx,newy,p+1])
                    
                    
        if ans == int(1e19):
            return -1
        
        return ans