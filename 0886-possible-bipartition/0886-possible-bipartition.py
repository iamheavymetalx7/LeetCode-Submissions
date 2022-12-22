'''
Multiple components!!

'''
from collections import defaultdict,deque
class Solution:
    def check(self,start,n,adj,color):
        q=deque()
        q.append(start)
        
        color[start-1]=0
        
        while q:
            node = q.popleft()
            
            for j in adj[node]:
                if color[j-1]==-1:
                    color[j-1]=1-color[node-1]
                    q.append(j)
                elif color[j-1]==color[node-1]:
                    return False    
        return True
                    
        
    
    
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
            adj=defaultdict(list)
            
            for x,y in dislikes:
                adj[x].append(y)
                adj[y].append(x)

            color=[-1]*(n)
                        
            for i in range(1,n+1):
                if color[i-1]==-1:
                    if self.check(i,n,adj,color)==False:
                        return False
            return True
                