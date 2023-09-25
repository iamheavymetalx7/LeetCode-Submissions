'''

https://leetcode.com/submissions/detail/808040794/
'''

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

    
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n=len(vals)
        
        g= [[] for _ in range(n)]
        
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        
        
        value_to_nodes = defaultdict(list)
        
        for i,val in enumerate(vals):
            value_to_nodes[val].append(i)
        # print(value_to_nodes)
        # print(g)
        
        dsu = UnionFind(n)
        
        isActive = [False for _ in range(n+1)]
        ans=n
        seen = sorted(set(vals))
        
        ## we go in increasing manner, then we activate them one by one
        
        for ele in seen:
            indexes = value_to_nodes[ele]
            for i in indexes:
                for child in g[i]:
                    if isActive[child]:
                        dsu.merge(i,child)
                isActive[i]=1
            
            leaders =[]
            for i in indexes:
                leaders.append(dsu.find(i))
            cnter =Counter(leaders)
            
            for i,v in cnter.items():
                ans+=(v*(v-1))//2
        return ans
        