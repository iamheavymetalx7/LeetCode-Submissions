class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        inf = int(1e19)
        n=len(grid)
        m=len(grid[0])
        
        g=[[] for _ in range(n*m)]
        
        dire = [(0,1),(1,0),(-1,0),(0,-1)]
        
        
        
        def calc_idx(i,j):
            return m*i+j
        
        for i in range(n):
            for j in range(m):
                for dx,dy in dire:
                    dx+=i
                    dy+=j

                    if 0<=dx<n and 0<=dy<m:
                        if grid[dx][dy]==1:
                            g[calc_idx(i,j)].append([calc_idx(dx,dy),1])
                        else:
                            g[calc_idx(i,j)].append([calc_idx(dx,dy),0])
                            
#         for i in range(n*m):
#             print(i,g[i])
        pq=[]
        dist=[inf for _ in range(n*m)]
        # print(n*m)
        src = 0
        dist[src]=0
        
        heappush(pq,[0,0])
        
        while pq:
            dis,u = heappop(pq)
            if dis>dist[u]:continue
            
            for v,c in g[u]:
                if dist[v]>dis+c:
                    dist[v]=dis+c
                    heappush(pq,[dis+c,v])
                
        
        return (dist[-1])
            