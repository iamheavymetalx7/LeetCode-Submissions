'''
reference : https://www.youtube.com/watch?v=Y9OQHKyhxGo

Dijkstra Modified

'''

class Solution:
    def minimumCost(self, st: List[int], tgt: List[int], specialRds: List[List[int]]) -> int:
        
        N = len(specialRds)
        inf = 10**20
        dist =[inf]*(N)
        
        best = abs(st[0]-tgt[0])+abs(st[1]-tgt[1])
        
        h=[]
        
        heappush(h,[0,st[0],st[1],-1])
        
        while h:
            d,x,y,i = heappop(h)
            
            if i!=-1 and dist[i]>d:
                continue
                
            best = min(best, d+abs(x-tgt[0])+abs(y-tgt[1]))
            
            for idx,(sx,sy,ex,ey,c) in enumerate(specialRds):
                cost = d+abs(sx-x)+abs(sy-y)+c
                
                if dist[idx]>cost:
                    dist[idx]=cost
                    heappush(h,[cost,ex,ey,idx])
        return best
                    
                