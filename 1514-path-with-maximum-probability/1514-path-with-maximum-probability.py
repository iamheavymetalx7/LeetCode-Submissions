class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        g = [[] for _ in range(n)]
        prob=[0 for _ in range(n)]
        for i in range(len(edges)):
            g[edges[i][0]].append([edges[i][1],succProb[i]])
            g[edges[i][1]].append([edges[i][0],succProb[i]])
    
        q = deque()
        q.append([1,start_node])
        prob[start_node]=1
        while q:
            ps,u = q.popleft()
            for v,p in g[u]:
                if prob[v]<ps*p:
                    prob[v]=ps*p
                    q.append([ps*p,v])
        
        return (prob[end_node])
                
                