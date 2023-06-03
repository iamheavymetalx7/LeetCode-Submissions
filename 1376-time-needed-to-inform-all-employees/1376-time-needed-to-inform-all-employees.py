class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        n=len(manager)
        dic=defaultdict(list)
        for i in range(n):
            if manager[i]==-1:
                continue
            dic[manager[i]].append([i, informTime[i]])
        print(dic)
        
        ans =[0]*(n)
        
        q=deque()
        vis=set()
        
        q.append([headID,informTime[headID]])
        vis.add(headID)
        
        while q:
            ele,time = q.popleft()
            ans[ele]=time
            
            for nei in dic[ele]:
                node,t =nei
                if node not in vis:
                    q.append([node,time+t])
                    vis.add(node)
        
        return max(ans)
