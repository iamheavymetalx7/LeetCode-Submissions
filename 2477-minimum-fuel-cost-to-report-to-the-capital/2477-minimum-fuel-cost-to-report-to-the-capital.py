from collections import defaultdict
import math
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        adj = defaultdict(list)
        
        for x,y in roads:
            adj[x].append(y)
            adj[y].append(x)
        
        
        def dfs(node, parent):
            nonlocal res
            passenger = 0
             
            for ele in adj[node]:
                if ele!=parent:
                    p = dfs(ele,node)
                    passenger+=p
                    res+=int(math.ceil(p/seats))
                    
            return passenger+1
                    
                    
                    
                    
            
        
        
        res=0
        
        dfs(0,-1)
        
        return res
        
            
        