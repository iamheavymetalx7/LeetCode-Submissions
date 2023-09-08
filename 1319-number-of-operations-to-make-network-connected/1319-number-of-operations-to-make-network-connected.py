class UnionFind:
    def __init__(self,n):
        self.par= [i for i in range(n)]
        self.rank =[1 for i in range(n)]
    
    def find(self,x):
        p=self.par[x]
        
        while p!=self.par[p]:
            self.par[p]=self.par[self.par[p]]
            p=self.par[p]
        return p
    
    def issame(self,x,y):
        p1,p2 = self.find(x),self.find(y)
        if p1==p2:
            return True
        return False
    
    def merge(self,x,y):
        p1,p2 = self.find(x),self.find(y)
        if p1==p2:
            return True
        
        if self.rank[p1]<self.rank[p2]:
            self.par[p1]=p2
            self.rank[p2]+=1
        else:
            self.par[p2]=p1
            self.rank[p1]+=1
            
        
        return False

            
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        uf= UnionFind(n)
        cnt=0
        
        for x,y in connections:
            if uf.issame(x,y):
                cnt+=1
            else:
                uf.merge(x,y)
        
        dic = defaultdict(list)
        
        for i in range(n):
            dic[uf.find(i)].append(i)
        

        
        if len(dic)-1 > cnt:
            return -1
        return len(dic)-1