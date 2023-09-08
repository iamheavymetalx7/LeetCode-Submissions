class UnionFind:
    def __init__(self,n):
        self.par =[i for i in range(n)]
        self.rank = [0 for i in range(n)]
    
    def find(self,x):
        p=self.par[x]
        
        while p!=self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p=self.par[p]
        return p
    def merge(self,x,y):
        p1,p2 = self.find(x),self.find(y)
        
        if p1==p2:
            return
        
        if self.rank[p1]<self.rank[p2]:
            self.rank[p2]+=1
            self.par[p1]=p2
        else:
            self.rank[p1]+=1
            self.par[p2]=p1
            

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
    
        
        uf = UnionFind(26)
        
        for e in equations:
            if e[1]=="=":
                uf.merge(ord(e[0])-ord('a'),ord(e[-1])-ord('a'))

        for e in equations:
            if e[1]=="!" and uf.find(ord(e[0])-ord('a')) == uf.find(ord(e[-1])-ord('a')):
                return False
        
        return True
        
        
            
            