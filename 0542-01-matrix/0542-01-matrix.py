class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        
        dire =[(0,1),(-1,0),(0,-1),(1,0)]
        m=len(mat)
        n=len(mat[0])
        
        vis=[[0]*n for _ in range(m)]

        ans=[[-1]*n for _ in range(m)]
        
        q=deque()
        
        dire=[(1,0),(-1,0),(0,1),(0,-1)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append([i,j,0])
                    vis[i][j]=1
                    
        
        while q:
            r,c,steps = q.popleft()
            ans[r][c]=steps
            
            for x,y in dire:
                nr = x+r
                nc = y+c
                
                if 0<=nr<m and 0<=nc<n and not vis[nr][nc]:
                    vis[nr][nc]=1
                    q.append([nr,nc,steps+1])
        return ans
            