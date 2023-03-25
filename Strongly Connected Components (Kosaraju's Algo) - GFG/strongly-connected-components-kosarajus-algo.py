#User function Template for python3

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        visited=set()
        stack=[]  
        # print(adj)
        
        def dfs(node):
            # print(node,"this is node in first dfs")
            visited.add(node)
            
            for it in adj[node]:
                if it not in visited:
                    dfs(it)
            
            
            stack.append(node)
        
        
        def dfs3(node):
            visited.add(node)
            for it in adjT[node]:
                if it not in visited:
                    dfs3(it,adj)
            
        

        for i in range(V):
            if i not in visited:
                dfs(i)
        
        # print(stack)
        
        
        adjT=[[] for _ in range(V)]
        # print(adjT)
        
        for i in range(V):
            visited.discard(i)
            for it in adj[i]:
                adjT[it].append(i)
        # print(adjT)
        scc=0
        while stack:
            ele = stack.pop()
            if ele not in visited:
                scc+=1
                dfs3(ele)
        
        return scc
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends