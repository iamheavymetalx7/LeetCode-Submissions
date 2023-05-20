class Solution:
    def calcEquation(self, equations: List[List[str]], val: List[float], queries: List[List[str]]) -> List[float]:
        n=len(queries)
        seen=set()
        
        n=len(queries)
        
        ans=[-1]*n
        
        graph=defaultdict(list)
        
        for i, (x,y) in enumerate(equations):
            seen.add(x)
            seen.add(y)
            graph[x].append([y,val[i]])
            graph[y].append([x,1/val[i]])
        
        
        def bfs(src,dst):
            q,seen = deque([(src,1.0)]),set()
            
            while q:
                x,v=q.popleft()
                if x==dst:
                    return v
                seen.add(x)
                
                for y,val in graph[x]:
                    if y not in seen:
                        q.append((y,v*val))
            return -1.0
                    
        
        for i,(x,y) in enumerate(queries):
            if x not in seen or y not in seen:
                continue
            
            ans[i] = bfs(x,y)
        
        return ans
                            
                    