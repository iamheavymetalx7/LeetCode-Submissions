#User function Template for python3
from collections import deque, defaultdict
class Solution:
    def findOrder(self, n, m, prerequisites):
        # Code here
        
        adj=defaultdict(list)
        
        for preq in prerequisites:
            adj[preq[1]].append(preq[0])
        
        indegree=[0]*n
        
        for i in range(n):
            for adjele in adj[i]:
                indegree[adjele]+=1
        topo=[]
        q=deque()
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
                
        while q:
            node=q.popleft()
            topo.append(node)
            
            for adjele in adj[node]:
                indegree[adjele]-=1
            
                if indegree[adjele]==0:
                    q.append(adjele)
        if len(topo)==n:
            return topo
        return []
        


#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
	map=[0]*N
	for i in range(N):
		map[res[i]]=i
	for i in range(N):
		for v in graph[i]:
			if map[i] > map[v]:
				return False
	return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,m = list(map(int, input().strip().split()))
        adj = [[] for i in range(n)]
        prerequisites = []
        
        for i in range(m):
            u,v=map(int,input().split())
            adj[v].append(u)
            prerequisites.append([u,v])
            
        ob = Solution()
        
        res = ob.findOrder(n, m, prerequisites)
        
        if(not len(res)):
            print("No Ordering Possible")
        else:
            if check(adj, n, res):
                print(1)
            else:
                print(0)
# } Driver Code Ends