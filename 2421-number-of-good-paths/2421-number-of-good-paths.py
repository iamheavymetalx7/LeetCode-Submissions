class UnionFind:
    def __init__(self,n):
        self.par =list(range(n))
        self.rank =[0]*n
    
    def find(self,i):
        
        while i!=self.par[i]:
            self.par[i]=self.par[self.par[i]]
            i=self.par[i]
        
        return i
    
    def union(self,a,b):
        aRoot = self.find(a)
        bRoot = self.find(b)
        
        if aRoot == bRoot:
            return False
        
        if self.rank[aRoot]<self.rank[bRoot]:
            self.rank[bRoot]+=self.rank[aRoot]
            self.par[aRoot] = bRoot
        else:
            self.rank[aRoot]+=self.rank[bRoot]
            self.par[bRoot] = aRoot
        
        return True
        
        
        


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        valsToIndex = defaultdict(list)
        
        for i,val in enumerate(vals):
            valsToIndex[val].append(i)
        
        
        res=0
        uf = UnionFind(len(vals))
        
        
        for val in sorted(valsToIndex.keys()):
            for i in valsToIndex[val]:
                for nei in adj[i]:
                    if vals[nei]<=vals[i]:
                        uf.union(nei,i)
                        
            # for each disjoint set, how many val's it contains?
            count = defaultdict(int)
            
            for i in valsToIndex[val]:
                count[uf.find(i)]+=1
                res+=count[uf.find(i)]
        return res
                    
                    
                
        
        
        
        

        