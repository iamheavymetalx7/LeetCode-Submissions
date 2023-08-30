class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD =int(1e9)+7
        inf = int(1e19)
        dist =[inf for _ in range(n)]
        ways=[0 for _ in range(n)]
        g =[[] for _ in range(n)]
        
        for x,y,c in roads:
            g[x].append([y,c])
            g[y].append([x,c])
        
        
        
        def dijkstra(src):
            dist[src] =0
            ways[0]=1
            heap =[]
            
            heappush(heap,[0,src])
            
            while heap:
                dis,u = heappop(heap)
                
                for v,c in g[u]:
                    ## first time arriving
                    if dist[v]>dis+c:
                        ways[v]=ways[u]
                        dist[v]=dis+c
                        heappush(heap,[dis+c,v])
                    elif dist[v]==dis+c:
                        ways[v]=(ways[v] + ways[u])%MOD
                    
                
        dijkstra(0)
        return (ways[-1]%MOD)