class UnionFind:
    def __init__(self,n):
        self.par = [i for i in range(n+1)]
        self.rank = [1 for i in range(n+1)]

    def find(self,x):
        p = self.par[x]
        
        while p!=self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p=self.par[p]
        
        return p
    
    def merge(self,x,y):
        p1 = self.find(x)
        p2= self.find(y)
        
        if p1==p2:
            return
        
        if self.rank[p1]>=self.rank[p2]:
            self.par[p2]=p1
            self.rank[p1]+=self.rank[p2]
        else:
            self.par[p1]=p2
            self.rank[p2]+=self.rank[p1]
            
    def size(self,x):
        return self.rank[self.find(x)]
    
mx=int(1e5)+1
sieve =[False,False]+[True for _ in range(mx+1)]
            
for i in range(2,int(math.sqrt(mx))+1):
    if sieve[i]:
        for j in range(i*i,mx+1,i):
            sieve[j]=False

def isPrime(x):
    if sieve[x]:
        return True


        
class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        
        g =[[] for _ in range(n+1)]
        
        uf = UnionFind(n)
        
        
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
            
            x_p = isPrime(x)
            y_p = isPrime(y)
            
            if (x_p or y_p):continue
            uf.merge(x,y)
        
        
        res =0
        for j in range(1,n+1):
            if not isPrime(j):
                continue
            
            nodes=[]
            sum=1
            
            for e in g[j]:
                if isPrime(e):
                    continue
                
                nodes.append(uf.size(e))
                sum+=nodes[-1]
                
            # print(j,"this primenode",nodes,sum)
            for ele in nodes:
                sum-=ele
                res+=sum*ele
        return res
                
            
        
        
        
        