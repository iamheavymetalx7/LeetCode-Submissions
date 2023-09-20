class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        l=-1
        r=int(2e5)
        n,m= len(grid),len(grid[0])
        
        dire = [(1,0),(0,1),(-1,0),(0,-1)]
        
        def check(mid):
            q=deque()
            vis=set()
            q.append((0,0))
            vis.add((0,0))
            if grid[0][0]>mid:
                return False
            
            while q:
                x,y = q.popleft()
                if x==n-1 and y==m-1:
                    return True
                for dx,dy in dire:
                    dx+=x
                    dy+=y
                    
                    if 0<=dx<n and 0<=dy<m and (dx,dy) not in vis and grid[dx][dy]<=mid:
                        q.append((dx,dy))
                        vis.add((dx,dy))
            return False
                
                        
        
        while r-l>1:
            mid =(l+r)//2
            
            if check(mid):
                r=mid
            else:
                l=mid
        return r
                