class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj =[[] for _ in range(n)]
        
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        ans=[0]*(n)
        subSize =[0]*(n)
        subAns= [0]*(n)
        
        def recur(u,p):
            numNodes=1
            anssubTree=0
            
            for v in adj[u]:
                if v!=p:
                    recur(v,u)
                    numNodes+=subSize[v]
                    anssubTree+=subAns[v]+subSize[v]
            subSize[u] = numNodes
            subAns[u] = anssubTree
        
        def solve(src,par,partial_ans,totalNodes):
            ans[src] = subAns[src]+partial_ans+totalNodes-subSize[src]
            
            for child in adj[src]:
                if child!=par:
                    solve(child,src,ans[src]-(subAns[child]+subSize[child]),totalNodes)
        
        recur(0,-1)
        solve(0,0,0,n)
        
        return ans
                    