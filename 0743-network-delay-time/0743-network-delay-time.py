from heapq import *
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        INF = int(1e9)
        graph = [[] for _ in range(n+1)]
        dist =[INF]*(n+1)
        
        for x,y,w in times:
            graph[x].append([y,w])
        
        dist[k] =0
        
        pq=[]
        heappush(pq,[0,k])
        
        while pq:
            dis,node = heappop(pq)
            
            for ele in graph[node]:
                if dis+ele[1]<dist[ele[0]]:
                    dist[ele[0]]=dis+ele[1]
                    heappush(pq,[dist[ele[0]],ele[0]])
        
        maxi = max(dist[1:])
        if maxi==INF:
            return -1
        return max(dist[1:])