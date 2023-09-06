class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        
        heap =[]
        g = [[] for _ in range(n)]
        
        for x,y,w in edges:
            g[x-1].append([y-1,w])
            g[y-1].append([x-1,w])
        
        inf = int(1e19)
        dist =[inf for _ in range(n)]
        
        dist[n-1] = 0
        
        heappush(heap,[0,n-1])
        
        while heap:
            dis,u = heappop(heap)
            if dis != dist[u]: continue
            for v,weight in g[u]:
                if dist[u]+weight<dist[v]:
                    dist[v]=dist[u]+weight
                    heappush(heap,[dist[v],v])

        MOD = int(1e9)+7
        
        
        @cache
        def dfs(src):
            if src == n-1:
                return 1
            ans = 0  
            for v,wt in g[src]:
                if dist[src]>dist[v]:
                    ans = (ans+dfs(v))%MOD
                    
            return ans
        return dfs(0)