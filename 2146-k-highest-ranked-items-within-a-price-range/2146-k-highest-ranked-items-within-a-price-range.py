class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        
        n,m=len(grid),len(grid[0])
        
        
        x0,y0 = start[:]
        
        vis=set()
        
        q=deque()
        heap =[]

        q.append([x0,y0,0])
        vis.add((x0,y0))
        
        dire =[(0,1),(1,0),(-1,0),(0,-1)]
        
        if pricing[0]<=grid[x0][y0]<=pricing[1]:
            heappush(heap,[0,grid[x0][y0],x0,y0])
        
        while q:
            x,y,dist = q.popleft()

            for dx,dy in dire:
                dx+=x
                dy+=y
                
                if 0<=dx<n and 0<=dy<m and (dx,dy) not in vis and grid[dx][dy]!=0:
                    price = grid[dx][dy]
                    if pricing[0]<=price<=pricing[1]:
                        q.append((dx,dy,dist+1))
                        vis.add((dx,dy))
                        heappush(heap,[dist+1,price,dx,dy])
                        
                    else:
                        q.append((dx,dy,dist+1))
                        vis.add((dx,dy))
        ans =[]
        for i in range(min(k,len(heap))):
            dd,pri,row,col = heappop(heap)
            ans.append([row,col])
        return ans
            
            
                
            