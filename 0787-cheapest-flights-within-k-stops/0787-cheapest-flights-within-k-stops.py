class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj =[[] for _ in range(n)]
        inf = int(1e19)
        for prv,nxt,cost in flights:
            adj[prv].append([nxt,cost])
        cost =[inf for _ in range(n)]
        q =deque()
        cost[src]=0
        q.append([0,src,0])
        
        while q:
            wt,node,stops = q.popleft()
            if stops>k:
                continue
            for el,wei in adj[node]:
                if cost[el]>wei+wt:
                    cost[el]=wei+wt 
                    q.append([wei+wt,el,stops+1])
        
        if cost[dst]==inf:
            return -1
        return cost[dst]