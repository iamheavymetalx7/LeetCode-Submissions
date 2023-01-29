from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here

        
        def solve(src):
            vis[src]=1
            q.append([src,-1])
        
            while q:
                node,par = q.popleft()
                
                for adjele in adj[node]:
                    if not vis[adjele]:
                        vis[adjele]=1
                        q.append([adjele,node])
                    else:
                        if par!=adjele:
                            return True
                        
            return False
                        
		
        q=deque()
        vis=[0]*V
        
        
        for i in range(V):
            if not vis[i]:
                if solve(i):
                    return True
        return False
                    
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
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends