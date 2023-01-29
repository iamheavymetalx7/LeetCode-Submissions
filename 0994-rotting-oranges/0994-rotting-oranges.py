from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dire=[(1,0),(0,1),(-1,0),(0,-1)]
        rotten=deque()
        
        

        total=0
        
        
        rot=0
        time=0
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    rotten.append([i,j])
                if grid[i][j]:
                    total+=1
        
        while rotten:
            t=len(rotten)
            rot+=t
            
            for j in range(t):
                x,y = rotten.popleft()
                
                for x_,y_ in (dire):
                    if 0<=x+x_<len(grid) and 0<=y+y_<len(grid[0]) and grid[x+x_][y+y_]==1:
                        grid[x+x_][y+y_]=2
                        rotten.append([x+x_,y+y_])
            if rotten:
                time+=1
            
        if rot==total:
            return time
        return -1

        
        
        