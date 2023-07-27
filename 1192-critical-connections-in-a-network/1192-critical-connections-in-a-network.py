class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        ## using tarjan's algorithm of time in and low-time
        ## striver
        ## hinT: Use Tarjan's algorithm.


        
        
        adj =[[] for _ in range(n)]
        
        for x,y in connections:
            adj[x].append(y)
            adj[y].append(x)
        
        vis = [0]*(n)
        tin =[0]*(n)
        low=[0]*(n)
        
        bridges =[]
        
        timer = 1
        
        
        
        def dfs(node, parent):
            nonlocal timer
            vis[node]=1
            tin[node]=timer
            low[node]=timer
            
            timer+=1
            
            for it in adj[node]:
                if it==parent:
                    continue
                if vis[it]==0:
                    dfs(it,node)
                    low[node] = min(low[node],low[it])
                    
                    ## node---it ? bridge?
                    
                    if low[it] > tin[node]:
                        bridges.append([node,it])
                        
                
                else:
                    low[node]=min(low[node],low[it])
        
        dfs(0,-1)
        
        return bridges
                    
            
            
            