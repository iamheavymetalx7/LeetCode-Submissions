class UnionFind:
    def __init__(self,n):
        self.par =[i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def find(self,node):
        p = self.par[node]
        
        while p!=self.par[p]:
            self.par[p]= self.par[self.par[p]]
            p=self.par[p]
        return p
    
    def same(self,a,b):
        if self.par[a]!=self.par[b]:
            return 0
        return 1
    
    def merge(self,a,b):
        
        p1,p2= self.find(a),self.find(b)
        if p1==p2:
            return 0
        if self.rank[p1]>self.rank[p2]:
            self.par[p2]=p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1]=p2
            self.rank[p2]+=self.rank[p1]
        return 1 
    
# A connected component is complete if and only if the number of edges in the component is equal to m*(m-1)/2, where m is the number of nodes in the component.        
        
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        uf = UnionFind(n)
        
        g =[[] for _ in range(n)]
        
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        
        res = n
        
        for x,y in edges:
            res-=uf.merge(x,y)
        
        # print(res,"connected components")
        if res==0:
            return 0
        print(uf.par)
        seen=set(uf.par)
        vis=[0]*(n)
        
        
        for ele in seen:
            q=deque()
            q.append(ele)
            vertices,edges= set([ele]),set()
            
            while q:
                node = q.popleft()
                
                vis[node]=1
                
                for adj in g[node]:
                    if not vis[adj]:
                        if (node,adj) in edges or (adj,node) in edges:
                            continue
                        
                        edges.add((node,adj))
                        
                        vertices.add(adj)
                        q.append(adj)
            if (len(vertices)*(len(vertices)-1))//2!=len(edges):
                res-=1
        return res
                
            
        
        
    