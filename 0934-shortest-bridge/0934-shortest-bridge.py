class Solution:
    ## combo of dfs and bfs!!
    
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        n=len(grid)
        m=len(grid[0])
        
        q=deque()
        dire =[(1,0),(0,1),(-1,0),(0,-1)]
        
        def invalid(r,c):
            return r<0 or r>=n or c<0 or c>=m
        
        visit=set()
        def dfs(r,c):
            if invalid(r,c) or not grid[r][c] or (r,c) in visit:
                return
            visit.add((r,c))

            for dr,dc in dire:
                dr+=r
                dc+=c
                dfs(dr,dc)
        
        def bfs():
            res,q =0, deque(visit)
            
            while q:
                for i in range(len(q)):
                    r,c=q.popleft()
                    
                    for dr,dc in dire:
                        dr+=r
                        dc+=c
                        
                        if invalid(dr,dc) or (dr,dc) in visit:
                            continue
                        
                        if grid[dr][dc]:
                            return res
                        
                        q.append((dr,dc))
                        visit.add((dr,dc))
                res+=1
    
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    dfs(i,j)
                    return bfs() 
        
                            
                            
                            
                        
                            
                    
                    
                    
                    
                    
                    
                    
        
        