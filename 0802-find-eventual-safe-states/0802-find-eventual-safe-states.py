class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        outdegree = [0]*len(graph)
        q=deque()
        for i in range(n):
            outdegree[i] =len(graph[i])
            
            if outdegree[i]==0:
                q.append(i)
        
        R = [[] for _ in range(n)]
        
        for i in range(n):
            for v in graph[i]:
                R[v].append(i)
                
        safe=[0]*(n)
        while q:
            node = q.popleft()
            safe[node]=1
            
            for v in R[node]:
                outdegree[v]-=1
                
                if outdegree[v]==0:
                    q.append(v)
        ans=[]
        for i,x in enumerate(safe):
            if x!=0:
                ans.append(i)
        return ans
        
            
        
        