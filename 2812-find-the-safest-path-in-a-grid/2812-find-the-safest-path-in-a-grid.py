class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        
        q=deque()
        n=len(grid)
        dire=[(1,0),(0,1),(0,-1),(-1,0)]
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    q.append((i,j))
        
        dist =0
        vis=set()
        dist_to_theif =[[-1]*n for _ in range(n)]
        
        while q:
            mm = len(q)
            for _ in range(mm):
                x,y = q.popleft()
                if dist_to_theif[x][y]==-1:
                    dist_to_theif[x][y] = dist

                for dx,dy in dire:
                    dx+=x;dy+=y

                    if 0<=dx<n and 0<=dy<n and (dx,dy) not in vis:
                        q.append((dx,dy))
                        vis.add((dx,dy))
            dist+=1
        
        l=-1;r=n+1
        
        def isPossible(mid):
            if dist_to_theif[0][0]<mid:
                return False
            q=deque()
            q.append((0,0))
            vis=set()
            vis.add((0,0))
            
            
            while q:
                x,y =q.popleft()
                if x==n-1 and y==n-1:
                    return True
                for dx,dy in dire:
                    dx+=x
                    dy+=y
                    if 0<=dx<n and 0<=dy<n and (dx,dy) not in vis:
                        if dist_to_theif[dx][dy]>=mid:
                            q.append((dx,dy))
                            vis.add((dx,dy))
            return False
                        
                    
        
        
        while r-l>1:
            mid =(l+r)//2
            if isPossible(mid):
                l=mid
            else:
                r=mid
        return l
                    
                    
                    
                    
            
            
        