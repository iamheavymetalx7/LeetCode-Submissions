class UnionFind:
    def __init__(self,n):
        self.par =[i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def find(self,node):
        p = self.par[node]
        
        while p!=self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p=self.par[p]
        return p
    
    def merge(self,x,y):
        p1,p2 = self.find(x),self.find(y)
        
        if self.rank[p1]>self.rank[p2]:
            self.par[p2]=p1
            self.rank[p1]+=self.rank[p2]
        else:
            self.par[p1]=p2
            self.rank[p2]+=self.rank[p1]
    
        

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        graph =[]
        n=len(points)
        
        def dist(a,b):
            x1,y1=a[:]
            x2,y2=b[:]
            
            return abs(x1-x2)+abs(y1-y2)
        
        for i in range(n):
            for j in range(i+1,n):
                graph.append([i,j,dist(points[i],points[j])])
        
        graph.sort(key = lambda x:x[2])
        
        # print(graph)
        uf = UnionFind(n)
        
        to_ret =0
        
        for x,y,dis in graph:
            if uf.find(x)==uf.find(y):
                continue
            else:
                to_ret+=dis
                uf.merge(x,y)
        
        return to_ret
        