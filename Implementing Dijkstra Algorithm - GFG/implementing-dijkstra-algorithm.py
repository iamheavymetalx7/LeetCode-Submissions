import math
from heapq import heapify, heappush, heappop
class Solution:
    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        pq=[]
        dist=[math.inf]*V
        
        dist[S]=0
        
        heappush(pq,[0,S])
        
        while pq:
            
            dis,node = heappop(pq)
        
            for adjNode,eW in adj[node]:
                
                if dis+eW < dist[adjNode]:
                    dist[adjNode]=dis+eW
                    heappush(pq,[dist[adjNode],adjNode])
                    
        return dist

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends