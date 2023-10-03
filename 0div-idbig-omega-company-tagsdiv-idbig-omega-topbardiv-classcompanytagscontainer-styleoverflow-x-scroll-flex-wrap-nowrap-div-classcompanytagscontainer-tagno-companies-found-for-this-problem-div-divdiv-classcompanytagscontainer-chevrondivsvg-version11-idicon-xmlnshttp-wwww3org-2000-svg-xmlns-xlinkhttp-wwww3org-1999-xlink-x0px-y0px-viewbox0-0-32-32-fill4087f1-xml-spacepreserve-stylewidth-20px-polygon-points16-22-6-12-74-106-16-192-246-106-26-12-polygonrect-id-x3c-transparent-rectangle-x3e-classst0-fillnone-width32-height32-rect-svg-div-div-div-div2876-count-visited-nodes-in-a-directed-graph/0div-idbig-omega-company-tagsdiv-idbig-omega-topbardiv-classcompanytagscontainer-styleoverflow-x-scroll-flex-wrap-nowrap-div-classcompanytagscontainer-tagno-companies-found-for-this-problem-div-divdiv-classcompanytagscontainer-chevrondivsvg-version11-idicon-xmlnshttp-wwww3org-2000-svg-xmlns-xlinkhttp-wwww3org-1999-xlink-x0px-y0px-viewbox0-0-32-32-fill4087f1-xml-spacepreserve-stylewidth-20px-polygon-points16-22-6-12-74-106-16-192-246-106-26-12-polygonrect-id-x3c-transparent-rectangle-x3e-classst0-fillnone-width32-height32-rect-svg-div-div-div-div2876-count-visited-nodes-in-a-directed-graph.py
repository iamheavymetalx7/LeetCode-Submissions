'''
they can still be in different components:
this test case: [6,3,6,1,0,8,0,6,6] (539/941)

the idea is that each node is contained in a cycle, or on traversing forwards reaches an cycle
'''

class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        
        topo =[]
        n=len(edges)
        
        indegree =[0 for _ in range(n)]
        vis= [0 for _ in range(n)]
        
        g =[[] for _ in range(n)]
        for i,j in enumerate(edges):
            g[i].append(j)
            indegree[j]+=1
        
        q=deque()
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        while q:
            node = q.popleft()
            vis[node]=1
            topo.append(node)
            
            for ele in g[node]:
                indegree[ele]-=1
                if indegree[ele]==0:
                    q.append(ele)
        
        dp =[0 for _ in range(n)]
                    
        def fillCycle(i):
            length=0
            while not vis[i]:
                vis[i]=True
                i=edges[i]
                length+=1
            
            dp[i] = length
            j = edges[i]
            while j!=i:
                dp[j]=length
                j = edges[j]
        
                    
        for i in range(n):
            if not vis[i]:
                fillCycle(i)
            
        while topo:
            node = topo.pop()
            dp[node] = 1+dp[edges[node]]
        return dp