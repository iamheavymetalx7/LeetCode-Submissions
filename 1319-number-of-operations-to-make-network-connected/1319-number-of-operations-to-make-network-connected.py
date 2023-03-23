from collections import defaultdict
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # print(len(connections))
        if len(connections)<(n-1):
            return -1
        
        vis=set()        
        graph=defaultdict(list)
        for x,y in connections:
            graph[x].append(y)
            graph[y].append(x)
        print(graph)
        components = 0
        
        def dfs(u):
            if u in vis:
                return
            vis.add(u)
            
            for v in graph[u]:
                dfs(v)


        for i in range(n):
            if i not in vis:
                dfs(i)
                components+=1
        
        return components-1