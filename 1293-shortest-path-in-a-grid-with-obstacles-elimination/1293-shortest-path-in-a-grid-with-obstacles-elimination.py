class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        n=len(grid)
        m=len(grid[0])
        
        q=deque()
        q.append((0,0,k,0))
        
        dire=[(0,1),(1,0),(-1,0),(0,-1)]
        
        
        ans=10**9
        seen=set()
        
        while q:
            x,y,ob,cnt=q.popleft()
            
            if x==n-1 and y==m-1:
                ans=min(ans,cnt)
            
            if (x,y,ob) in seen:
                continue
            else:
                seen.add((x,y,ob))
                
            
            for dx,dy in dire:
                dx+=x
                dy+=y
            
                
                if 0<=dx<n and 0<=dy<m:
                    if grid[dx][dy]==0:
                        q.append((dx,dy,ob,cnt+1))
                    elif grid[dx][dy]==1 and ob>0:
                        q.append((dx,dy,ob-1,cnt+1))
        
        if ans==10**9:
            return -1
        return ans