class UnionFind:
    def __init__(self,n):
        self.rank =[1 for i in range(n)]
        self.par = [ i for i in range(n)]
        self.cnt =n
    def find(self,x):
        p = self.par[x]
        
        while p!=self.par[p]:
            self.par[p]=self.par[self.par[p]]
            p=self.par[p]
        return p

    def merge(self,x,y):
        p1,p2 = self.find(x),self.find(y)
        
        if p1==p2:
            return True
        self.cnt-=1
        if self.rank[p1]>self.rank[p2]:
            self.par[p2]=p1
            self.rank[p1]+=1
        else:
            self.rank[p2]+=1
            self.par[p1]=p2
        return False
    
    def getCount(self):
        return self.cnt
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n=len(stones)
        uf = UnionFind(n)
        
        def isConnected(p1,p2):
            if p1[0]==p2[0] or p1[1]==p2[1]:
                return True
            return False
        
        for i in range(n):
            for j in range(i+1,n):
                if isConnected(stones[i],stones[j]):
                    uf.merge(i,j)
        
        return n - uf.getCount()
        
                
                