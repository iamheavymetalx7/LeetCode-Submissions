class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        minHeap =[(0,0,0)]
        
        n=len(heights)
        m=len(heights[0])
        
        dist =[[int(1e19)]*(m) for _ in range(n)]
        dist[0][0]=0
        
        dire =[(1,0),(0,1),(-1,0),(0,-1)]
        
        while minHeap:
            dis,x,y = heappop(minHeap)
            
            if x==n-1 and y==m-1:
                return dis
            
            if dis>dist[x][y]:  ## it is outdated
                continue
            # print(dis,x,y)

            for dx,dy in dire:
                dx+=x   
                dy+=y
                if 0<=dx<n and 0<=dy<m:
                    newdis = max(dis,abs(heights[dx][dy]-heights[x][y]))  ## this is calc at each step
                    if newdis < dist[dx][dy]:
                        dist[dx][dy]=newdis
                        heappush(minHeap,[newdis,dx,dy])
                        
                    
                
            