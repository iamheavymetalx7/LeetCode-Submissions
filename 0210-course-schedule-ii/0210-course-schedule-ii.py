class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        gr= [[]for _ in range(n)]
        indegree =[0]*(n)
        
        for x,y in pre:
            gr[y].append(x)
            indegree[x]+=1
        
        q=deque()
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        
        ans=[]
        while q:
            node = q.popleft()
            ans.append(node)
            
            for nei in gr[node]:
                indegree[nei]-=1
                
                if indegree[nei]==0:
                    q.append(nei)
        
        if len(ans)!=n:
            return []
        return ans