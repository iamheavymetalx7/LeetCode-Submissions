class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        W =27
        g =[[] for _ in range(n+1)]
        lvl =[0 for _ in range(n+1)]
        par =[[0]*(n+1) for _ in range(15)]
        frq =[[0]*(W) for _ in range(n+1)]
        
        for x,y,w in edges:
            g[x+1].append([y+1,w])
            g[y+1].append([x+1,w])
        result =[]

        def dfs(src,parent):
            lvl[src]=lvl[parent]+1
            
            par[0][src] = parent
            
            for j in range(1,15):
                x = par[j-1][src]
                par[j][src] = par[j-1][x]
            
            
            for child,wei in g[src]:

                if child==parent:
                    continue
                
                frq[child] = frq[src][:]
                frq[child][wei]+=1
                 
                dfs(child,src)
        
        def LCA(u,v):
            if lvl[u]>lvl[v]:
                  u,v=v,u
            diff = lvl[v]-lvl[u]
            
            for j in range(0,15):
                if diff&(1<<j):
                    v=par[j][v]
            
            if u==v:return u
            
            for j in range(14,-1,-1):
                if par[j][u]!=par[j][v]:
                    u = par[j][u]
                    v = par[j][v]
            
            return par[0][u]
        
        
        dfs(1,0)

        for q1,q2 in queries:
            q1+=1
            q2+=1
            
            lca = LCA(q1,q2)
            
            freq_fin = [0 for _ in range(W)]
            for j in range(W):
                freq_fin[j] = frq[q1][j]+frq[q2][j]-2*frq[lca][j]
            
            
            mx,s=0,0
            for ele in freq_fin:
                mx=max(mx,ele)
                s+=ele
            
            result.append(s-mx)
            
        
        return result
                
                
        