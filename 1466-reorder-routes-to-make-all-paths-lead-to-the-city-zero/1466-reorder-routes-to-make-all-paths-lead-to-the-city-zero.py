from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # start at city 0
        # recursively cehck its neighbours
        # count outgoing edges
        
        edges = {(x,y) for x,y in connections}
        neighbors=defaultdict(list)
        
        visited=set()
        res=0
        
        for a,b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        def dfs(city):
            nonlocal edges, neighbors, visited, res
            
            
            for adj in neighbors[city]:
                if adj in visited:
                    continue
                
                # check if adj can reach 0
                
                if (adj,city) not in edges:
                    res+=1
                visited.add(adj)
                dfs(adj)
        visited.add(0)
        dfs(0)
        return res
                    
        
        