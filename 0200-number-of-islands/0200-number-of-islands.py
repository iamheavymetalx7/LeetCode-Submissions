class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        dire =[(1,0),(0,1),(-1,0),(0,-1)]
        
        n,m=len(grid),len(grid[0])
        
        cnt=0
        print(n,m)
        
        seen=set()
        
        if m==0:
            return cnt
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    
                    q=deque([(i,j)])
                    
                    while q:
                        x,y = q.popleft()
                        grid[x][y]="0"
                        if (x,y) in seen:
                            continue
                        else:
                            seen.add((x,y))
                        
                        for dx,dy in dire:
                            dx+=x
                            dy+=y
                            
                            if 0<=dx<n and 0<=dy<m and grid[dx][dy]=="1":
                                q.append((dx,dy))
                    cnt+=1
        return cnt
        