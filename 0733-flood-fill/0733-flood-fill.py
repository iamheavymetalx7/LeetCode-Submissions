class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque([(sr,sc)])
        n,m=len(image),len(image[0])
        
        curr = image[sr][sc]
        dire =[(1,0),(0,1),(-1,0),(0,-1)]
        
        image[sr][sc]=color
        seen=set()
        while q:
            x,y = q.popleft()
            
            if (x,y) in seen:
                continue
            else:
                seen.add((x,y))
            for dx,dy in dire:
                dx+=x
                dy+=y
                
                if 0<=dx<n and 0<=dy<m and image[dx][dy]==curr:
                    image[dx][dy]=color
                    q.append((dx,dy))
        return image