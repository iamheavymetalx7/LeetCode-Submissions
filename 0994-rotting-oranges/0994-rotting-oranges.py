class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_cnt= 0
        rotten = deque()
        
        n=len(grid)
        m=len(grid[0])
        vis=set()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    rotten.append((i,j))
                    vis.add((i,j))
                if grid[i][j]==1:
                    fresh_cnt+=1
        
        # print(rotten,"prifingal")
        
        dire =[(1,0),(0,1),(-1,0),(0,-1)]
        time=0
        
        while rotten:
            l=len(rotten)
            # print(rotten,l)
            for _ in range(l):
                x,y = rotten.popleft()
                
                for dx,dy in dire:
                    dx+=x
                    dy+=y
                    
                    # print(dx,dy,"inside for")
                    
                    
                    
                    if (dx,dy) not in vis: 
                        if 0<=dx<n and 0<=dy<m and grid[dx][dy]==1:
                            fresh_cnt-=1
                            vis.add((dx,dy))
                            rotten.append((dx,dy))
            if rotten:
                time+=1

        if fresh_cnt==0:
            return time
        return -1