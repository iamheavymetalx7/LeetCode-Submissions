from collections import Counter, defaultdict


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        gr=defaultdict(list)
        path=set()
        
        for i in range(len(roads)):
            gr[roads[i][0]].append([roads[i][1],roads[i][2]])
            gr[roads[i][1]].append([roads[i][0],roads[i][2]])
        
        vis=set()
        
        def dfs(u):
            if u in vis:
                return
            vis.add(u)
            
            for v,n in gr[u]:
                path.add(n)
                dfs(v)
        dfs(1)
        return min(path)