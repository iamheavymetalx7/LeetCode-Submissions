class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = len(prerequisites)
        indegree=[0]*(numCourses)
        
        dic = defaultdict(list)
        for x,y in prerequisites:
            dic[x].append(y)
            indegree[y]+=1
        
        q=deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        
        a=[]
        while q:
            node = q.popleft()
            a.append(node)
            for nei in dic[node]:
                indegree[nei]-=1
                
                if indegree[nei]==0:
                    q.append(nei)
        
        if len(a)==numCourses:
            return True
        
        return False
        
        
        