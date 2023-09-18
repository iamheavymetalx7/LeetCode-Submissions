class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        q=deque()
        INF = int(1e19)
        
        n,m=len(grid),len(grid[0])

        dist = [[INF] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    q.append((i,j,0))
                    dist[i][j] = 0

   
        dire =[(1,0),(0,-1),(0,1),(-1,0)]          
        while q:
            r,c,t = q.popleft()
            for dr,dc in dire:
                dr+=r
                dc+=c
                if 0<=dr<n and 0<=dc<m and dist[dr][dc]==INF and grid[dr][dc]!=2:
                    q.append((dr,dc,t+1))
                    dist[dr][dc]=t+1

        
        def isPossible(mid):
            q=deque()
            q.append((0,0,mid))
            
            d2 =[[INF]*(m) for _ in range(n)]
            
            if dist[0][0]<=mid:
                return False
            
            while q:
                x,y,t = q.popleft()

                for dx,dy in dire:
                    dx+=x
                    dy+=y
                    if 0<=dx<n and 0<=dy<m and d2[dx][dy]==INF and grid[dx][dy]!=2 and t+1<dist[dx][dy]:
                        d2[dx][dy]=t+1
                        q.append((dx,dy,t+1))
                        if dx==n-1 and dy==m-1:
                            return True
                    if dx==n-1 and dy==m-1 and d2[dx][dy]==INF and grid[dx][dy]!=2 and t+1<=dist[dx][dy]:
                        return True
                        
            return False
                    
                
            
        l,r=-1,int(2e4)+1
        
        while r-l>1:
            mid =(l+r)//2
            if isPossible(mid):
                l=mid
            else:
                r=mid
        return l if l!=int(2e4) else 10**9
            