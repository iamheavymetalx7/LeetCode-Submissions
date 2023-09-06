'''
we will use a ping-pong dijkstra
https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/discuss/3230800/C%2B%2B-Java-Python-Ping-Pong-Dijkstra
'''
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        heap =[]
        
        if grid[0][1]>1 and grid[1][0]>1:
            return -1
        
        heappush(heap,[grid[0][0],0,0])
        
        n=len(grid)
        m=len(grid[0])
        dire = [(0,1),(-1,0),(1,0),(0,-1)]
        vis=set()
        vis.add((0,0))
        while heap:
            time,x,y = heappop(heap)
            if x==n-1 and y==m-1:
                return time
            
            for dx,dy in dire:
                dx+=x
                dy+=y
                if 0<=dx<n and 0<=dy<m and (dx,dy) not in vis:
                    wait = 1 if (grid[dx][dy]-time)%2==0 else 0
                    vis.add((dx,dy))
                    heappush(heap,[max(time+1,grid[dx][dy]+wait),dx,dy])
            
                    
        return -1