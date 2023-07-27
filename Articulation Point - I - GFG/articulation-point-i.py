#User function Template for python3

import sys
sys.setrecursionlimit(10**6)

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, n, adj):
        # code here

        vis =[0]*(n)
        tin =[0]*(n)
        low =[0]*(n)
        mrk= [0]*(n)
        
        

        
        timer = 1
        
        def dfs(node,par):
            nonlocal timer
            vis[node]=1
            low[node]=timer
            tin[node]=timer
            
            timer+=1
            
            child =0
            
            for it in adj[node]:
                if it==par:
                    continue
                if not vis[it]:
                    dfs(it,node)
                    low[node]=min(low[node],low[it])

                    if low[it]>=tin[node] and par!=-1:
                        mrk[node]=1
                    child+=1
                        
                else:
                    low[node]=min(low[node],tin[it])
                    
            if child>1 and par==-1:
                mrk[node]=1
        
        
        for i in range(n):
            if not vis[i]:
                dfs(i,-1)
        
        ans =[]
        for i in range(n):
            if mrk[i]:
                ans.append(i)
        # print(ans)
        if not ans:
            return [-1]
        return ans

#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		ob = Solution()
		ans = ob.articulationPoints(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends