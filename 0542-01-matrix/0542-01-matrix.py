class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n,m = len(mat),len(mat[0])
        print(n,m)
        distance = [[0]*m for _ in range(n)]
        
        dire=[(1,0),(-1,0),(0,1),(0,-1)]        

                        
        q=deque()
        vis=[[0]*m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    q.append((i,j,0))
                    vis[i][j]=1
        
        while q:
            r,c,steps = q.popleft()
            distance[r][c]=steps
            
            for dx,dy in dire:
                dx+=r
                dy+=c
                if 0<=dx<n and 0<=dy<m and not vis[dx][dy]:
                    vis[dx][dy]=1
                    q.append((dx,dy,steps+1))
        
        
        
                    
        return distance
    
        

        