class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par =[i for i in range(len(edges)+1)]
        rank =[1 for _ in range(len(edges)+1)]
        
        
        def find(node):
            p = par[node]
            
            while p!=par[p]:
                par[p] = par[par[p]]
                p=par[p]
            
            return p
        
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            
            if p1==p2:
                return False
            
            if rank[p1]>rank[p2]:
                rank[p1]+=rank[p2]
                par[p2]=p1
            else:
                rank[p2]+=rank[p1]
                par[p1]=p2
            
            return True
        
        for x,y in edges:
            if not union(x,y):
                return [x,y]
        