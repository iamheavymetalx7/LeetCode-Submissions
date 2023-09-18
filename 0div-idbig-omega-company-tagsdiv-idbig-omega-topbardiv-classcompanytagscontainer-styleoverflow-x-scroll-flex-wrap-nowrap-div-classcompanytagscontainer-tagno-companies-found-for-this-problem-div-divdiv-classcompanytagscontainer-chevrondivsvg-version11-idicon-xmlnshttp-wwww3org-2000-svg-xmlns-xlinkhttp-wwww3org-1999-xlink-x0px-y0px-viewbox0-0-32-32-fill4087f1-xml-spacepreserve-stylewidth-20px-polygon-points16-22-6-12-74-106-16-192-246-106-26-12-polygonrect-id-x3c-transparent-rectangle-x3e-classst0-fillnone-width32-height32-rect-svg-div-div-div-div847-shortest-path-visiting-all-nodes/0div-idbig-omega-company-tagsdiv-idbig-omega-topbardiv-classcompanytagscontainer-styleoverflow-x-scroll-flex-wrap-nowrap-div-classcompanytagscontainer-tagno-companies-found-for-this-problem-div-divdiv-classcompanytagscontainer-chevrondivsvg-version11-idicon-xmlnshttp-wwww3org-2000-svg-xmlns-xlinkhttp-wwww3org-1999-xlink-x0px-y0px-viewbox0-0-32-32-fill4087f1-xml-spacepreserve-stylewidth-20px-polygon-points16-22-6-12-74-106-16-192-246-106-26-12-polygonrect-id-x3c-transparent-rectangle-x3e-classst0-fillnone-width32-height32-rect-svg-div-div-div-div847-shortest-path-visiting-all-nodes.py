'''
NOT your classic BFS    
1. https://leetcode.com/problems/shortest-path-visiting-all-nodes/discuss/4053514/94.74-BFS-%2B-Bitmask
2. https://www.youtube.com/watch?v=oof9-RLoFXQ
'''

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        q=deque()
        seen=set()
        
        n=len(graph)
        
        allVis = (1<<n)-1
        
        for i in range(n):
            q.append((i,1<<i,0))
            seen.add((i,1<<i))
        
        shortestPath = int(1e19)
        
        while q:
            node,currVis,lvl = q.popleft()
            if currVis == allVis:
                shortestPath = min(shortestPath,lvl)
                break
            
            for v in graph[node]:
                if (v, currVis|(1<<v)) not in seen:
                    q.append((v,currVis|(1<<v),lvl+1))
                    seen.add((v,currVis|(1<<v)))
        return shortestPath