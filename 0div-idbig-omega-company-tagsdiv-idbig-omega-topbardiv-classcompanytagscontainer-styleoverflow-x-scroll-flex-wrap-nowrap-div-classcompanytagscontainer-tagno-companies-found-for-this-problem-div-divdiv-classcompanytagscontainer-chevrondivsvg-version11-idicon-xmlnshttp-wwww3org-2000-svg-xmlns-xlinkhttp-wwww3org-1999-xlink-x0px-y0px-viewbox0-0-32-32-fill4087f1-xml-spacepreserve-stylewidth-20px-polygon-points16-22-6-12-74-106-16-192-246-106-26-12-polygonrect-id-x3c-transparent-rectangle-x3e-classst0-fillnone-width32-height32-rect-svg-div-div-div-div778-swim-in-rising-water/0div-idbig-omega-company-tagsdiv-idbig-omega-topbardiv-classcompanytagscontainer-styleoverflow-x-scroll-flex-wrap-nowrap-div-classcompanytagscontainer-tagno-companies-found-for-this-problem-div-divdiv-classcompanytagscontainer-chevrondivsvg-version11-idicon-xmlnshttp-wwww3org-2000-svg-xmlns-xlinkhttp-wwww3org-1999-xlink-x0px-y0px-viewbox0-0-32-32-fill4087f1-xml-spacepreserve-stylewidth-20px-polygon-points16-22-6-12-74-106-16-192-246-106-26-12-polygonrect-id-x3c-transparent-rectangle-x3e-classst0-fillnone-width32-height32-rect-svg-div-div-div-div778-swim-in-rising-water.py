class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        pq=[(grid[0][0],0,0)]
        n=len(grid)
        seen=set([(0,0)])
        res=0
        
        dire =[(1,0),(-1,0),(0,1),(0,-1)]
        while pq:
            val,x,y = heappop(pq)
            
            res = max(res,val)
            if x==n-1 and y==n-1:
                return res
            
            for dx,dy in dire:
                dx+=x
                dy+=y
                if 0<=dx<n and 0<=dy<n and (dx,dy) not in seen:
                    seen.add((dx,dy))
                    heappush(pq,(grid[dx][dy],dx,dy))
        
                
            