#User function Template for python3
from heapq import *
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        vis =[0]*(V)
        
        pq=[]
        heappush(pq,[0,0])#wt,node
        
        summ=0
        
        while pq:
            wt,node = heappop(pq)
            
            if vis[node]:
                continue
            vis[node]=1
            
            summ+=wt
            
            
            for nei in adj[node]:
                if not vis[nei[0]]:
                    heappush(pq,[nei[1],nei[0]])
        
        
        return summ
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends