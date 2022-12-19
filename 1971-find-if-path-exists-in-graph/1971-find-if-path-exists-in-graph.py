from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph=defaultdict(list)
        
        if not edges:
            return True
        
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        vis=set()
        def dfs(sc, dst):
            if dst in graph[sc]:
                return True
            if sc in vis:
                return False
            
            vis.add(sc)
            
            for x in graph[sc]:
                if dfs(x,destination):
                    return True
            return False
        
        return dfs(source,destination)
        
        