class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        
        color =[-1]*(n)
        
        q=deque()
        
        for i in range(n):
            if (color[i]==-1):
                color[i]=1
                q.append(i)
                
                while q:
                    cur=q.popleft()
                    
                    for nei in graph[cur]:
                        if color[nei]==-1:
                            color[nei]=1-color[cur]
                            q.append(nei)
                        else:
                            if color[nei]==color[cur]:
                                return False
        return True
                    

                    
# class Solution:
#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         n=len(graph)
        
#         color=[0]*(n)
        
#         q=deque()
        
#         for i in range(n):
#             if color[i]:
#                 continue
            
#             color[i]=1
#             q.append(i)
#             while q:
#                 cur=q.popleft()
#                 for neigh in graph[cur]:
#                     if not color[neigh]:
#                         color[neigh]=-color[cur]
#                         q.append(neigh)
#                     else:
#                         if color[neigh]==color[cur]:
#                             return False
#         return True
        

                    
                                        

                    
                