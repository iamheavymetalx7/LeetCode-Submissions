#User function Template for python3

from typing import List
from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        arr=[]
        q=deque()
        q.append(0)
        vis=set()
        while q:
            node=q.popleft()
            if node not in vis:
                vis.add(node)
                arr.append(node)
                for ad in adj[node]:
                    q.append(ad)
        return arr
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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends