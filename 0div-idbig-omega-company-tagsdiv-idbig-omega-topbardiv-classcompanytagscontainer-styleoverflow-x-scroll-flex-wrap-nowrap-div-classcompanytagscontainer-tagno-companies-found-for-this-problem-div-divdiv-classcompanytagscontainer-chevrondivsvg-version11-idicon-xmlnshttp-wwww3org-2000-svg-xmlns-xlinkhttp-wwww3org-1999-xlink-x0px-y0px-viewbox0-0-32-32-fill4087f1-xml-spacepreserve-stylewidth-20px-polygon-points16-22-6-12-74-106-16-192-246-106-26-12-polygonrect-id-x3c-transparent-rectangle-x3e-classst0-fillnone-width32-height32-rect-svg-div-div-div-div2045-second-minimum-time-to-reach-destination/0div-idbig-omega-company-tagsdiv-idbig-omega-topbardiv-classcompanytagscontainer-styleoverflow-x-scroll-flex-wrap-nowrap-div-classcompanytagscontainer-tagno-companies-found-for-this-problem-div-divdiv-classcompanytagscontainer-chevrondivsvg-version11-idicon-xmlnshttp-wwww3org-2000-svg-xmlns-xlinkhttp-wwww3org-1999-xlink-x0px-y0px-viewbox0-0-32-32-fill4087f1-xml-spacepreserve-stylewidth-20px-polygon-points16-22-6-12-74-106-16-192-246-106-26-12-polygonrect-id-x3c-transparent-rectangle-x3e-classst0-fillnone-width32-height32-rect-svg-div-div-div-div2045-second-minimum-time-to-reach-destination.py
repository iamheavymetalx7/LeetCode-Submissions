'''
prev submission was dijkstra, this is BFS only
'''



class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        inf = int(1e18)        
        
        graph =[[] for _ in range(n+1)]
        
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        
        dist=[[inf,inf] for _ in range(n+1)]
        
        dist[1][0]=0
        
        q=deque()
        q.append((1,0)) ## (node,dist)
        
        while q:
            u,dis = q.popleft()
            
            signal = dis//change
            
            if signal%2:
                dis+=((signal+1)*change - dis)
                
            dis+=time
            
            for v in graph[u]:
                if dist[v][0]>dis:
                    dist[v][0]=dis
                    q.append((v,dis))
                elif (dis>dist[v][0] and dis<dist[v][1]):
                    if v==n:
                        return dis
                    dist[v][1]=dis
                    q.append((v,dis))
        print(dist)
        return -1