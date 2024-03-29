class Solution:
	def isBipartite(self, V, adj):
		#code here
		
		color=[-1]*V
		
		def dfs(node,clr):
            color[node]=clr
            
		    for ele in adj[node]:
		        if color[ele]==-1:
		            color[ele]=1-color[node]
		            if dfs(ele,color[ele])==False:
		                return False
		        else:
		            if color[ele]==color[node]:
		                return False
		    return True
	    
	    for i in range(V):
	        if color[i]==-1:
	            if dfs(i,0)==False:
	                return False
	    return True
	           


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends