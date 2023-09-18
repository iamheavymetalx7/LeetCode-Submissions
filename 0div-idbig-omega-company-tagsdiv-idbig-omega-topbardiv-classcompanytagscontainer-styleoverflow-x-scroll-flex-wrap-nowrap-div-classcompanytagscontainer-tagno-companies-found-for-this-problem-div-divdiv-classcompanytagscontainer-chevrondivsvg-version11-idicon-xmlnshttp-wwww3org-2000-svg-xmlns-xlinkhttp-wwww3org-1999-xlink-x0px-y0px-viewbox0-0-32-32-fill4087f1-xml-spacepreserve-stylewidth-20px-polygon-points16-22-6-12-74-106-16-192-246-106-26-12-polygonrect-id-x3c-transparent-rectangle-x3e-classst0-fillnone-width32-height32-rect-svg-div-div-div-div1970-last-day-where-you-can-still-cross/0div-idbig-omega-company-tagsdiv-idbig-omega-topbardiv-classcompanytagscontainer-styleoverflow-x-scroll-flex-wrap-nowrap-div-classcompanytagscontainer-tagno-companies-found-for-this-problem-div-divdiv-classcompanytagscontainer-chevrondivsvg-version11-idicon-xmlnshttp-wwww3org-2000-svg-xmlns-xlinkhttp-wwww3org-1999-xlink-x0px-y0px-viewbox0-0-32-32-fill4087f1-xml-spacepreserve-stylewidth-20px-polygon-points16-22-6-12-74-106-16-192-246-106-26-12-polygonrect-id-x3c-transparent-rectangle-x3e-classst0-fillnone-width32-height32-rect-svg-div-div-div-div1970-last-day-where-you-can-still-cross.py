class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        dire = [(1,0),(0,1),(-1,0),(0,-1)]
        
        def isPossible(day):
            mat =[[0]*(col) for _ in range(row)]
            
            for i in range(day):
                x,y = cells[i]
                mat[x-1][y-1]=1
            
            q=deque()
            vis=set()
            for j in range(col):
                if mat[0][j]==0:
                    q.append((0,j))
                    vis.add((0,j))
            
            while q:
                r,c = q.popleft()
                if r==row-1:
                    return True
                for dr,dc in dire:
                    dr+=r
                    dc+=c
                    
                    if 0<=dr<row and 0<=dc<col and (dr,dc) not in vis and mat[dr][dc]==0:
                        q.append((dr,dc))
                        vis.add((dr,dc))
            
            return False
            
        
        l=-1
        r=row*col+1
        
        while r-l>1:
            mid = (l+r)//2
            if isPossible(mid):
                l=mid
            else:
                r=mid
        return l
            