class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        routes_set =[]
        if S==T:
            return 0
        
        ## creating for easy O(1) asymptotic search
        for r in routes:
            routes_set.append(set(r))
            
            
        graph = defaultdict(set)
        
        for i,r1 in enumerate(routes_set):
            for j in range(i+1,len(routes_set)):
                r2 = routes_set[j]
                
                for ele in r1:
                    if ele in r2:
                        graph[i].add(j)
                        graph[j].add(i)
        
        seen,targets = set(),set()
        
        for idx, route in enumerate(routes_set):
            if S in route:
                seen.add(idx)
            if T in route:
                targets.add(idx)
                
        q = deque()
        
        ## these have to take atleast one bus starting from source
        for node in seen:
            q.append((node,1))
        
        while q:
            node,depth = q.popleft()
            if node in targets:     ## this bus can take us to target, no need to change
                return depth
            
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei,depth+1))
        return -1
        
        
                        
            
        
        
