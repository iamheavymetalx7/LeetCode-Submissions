class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        
        inf = int(1e18)
        dist =[inf for _ in range(n+1)]
        
        dist[1]=0
        
        freq =defaultdict(int)
        freq[1]=1
        
        graph =[[] for _ in range(n+1)]
        
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        minheap =[]
        
        heappush(minheap,[0,1])
        flag=False
        
        while minheap:
            d,node = heappop(minheap)
            signal = d//change

            if signal%2:
                d+=((change)*(signal+1)-d)

            for nei in graph[node]:
                
                if dist[nei]!=d+time and freq[nei]<2:
                    if nei==n and flag:
                        return d+time
                    
                    if nei==n:
                        flag=True
                    
                    dist[nei]=d+time
                    freq[nei]+=1
                    heappush(minheap,[d+time,nei])
        