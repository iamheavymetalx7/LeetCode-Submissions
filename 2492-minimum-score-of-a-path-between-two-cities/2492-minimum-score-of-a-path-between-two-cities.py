from collections import defaultdict
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        gr=defaultdict(list)
        path = set()
        for src,dst,dist in roads:
            gr[src].append([dst,dist])
            gr[dst].append([src,dist])
        
        vis=set()
        
        def dfs(u):
            if u in vis:
                return
            
            vis.add(u)
            
            for x,y in gr[u]:
                path.add(y)
                dfs(x)
        dfs(1)
        return min(path)
                
                
                