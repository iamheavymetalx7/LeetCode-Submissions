class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=defaultdict(list)
        
        for flight in flights:
            adj[flight[0]].append([flight[1],flight[2]]) #source : [dest, cost]
        
        q=deque()
        
        q.append([0,src,0])
        
        dist =[pow(10,9)]*n
        dist[src]=0
        
        
        while q:
            stops,node,cost=q.popleft()
            
            if stops>k:
                continue
            
            
            for j in adj[node]:
                adjNode=j[0]
                edWeight=j[1]
                
                if cost+edWeight < dist[adjNode] and stops<=k:
                    dist[adjNode] = cost+edWeight
                    q.append([stops+1,adjNode,dist[adjNode]])
        if dist[dst]==pow(10,9):
            return -1
        return dist[dst]
                
            
        
        
            
        