class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color = [-1]*(n)
        
        q=deque()
        for i in range(n):
            q.append(i)
        
        
            while q:
                node = q.popleft()
                
                if color[node]==-1:
                    color[node]=0
                
                
                for adj in graph[node]:
                    # if adj==node:
                    #     continue

                    if color[adj]==-1:
                        color[adj]=1-color[node]
                        q.append(adj)
                    elif color[adj]==color[node]:
                        return False
        return True
                    
