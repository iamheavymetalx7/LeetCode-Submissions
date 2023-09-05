class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        g= [[] for _ in range(n)]
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        
        subTreeAns =[0]*(n)
        subTreeSize = [0]*(n)
        ans = [0]*(n)
        
        
        def dfs(src,par):
            numofNodes =1
            ansforSubTree = 0
            
            for child in g[src]:
                if child!=par:
                    dfs(child,src)

                    numofNodes += subTreeSize[child]
                    ansforSubTree += subTreeSize[child]+subTreeAns[child]
            
            subTreeSize[src] = numofNodes
            subTreeAns[src] = ansforSubTree
        
        
        def solve(src,par,partial_ans,total_nodes):
            
            ans[src] = subTreeAns[src]+partial_ans+(total_nodes-subTreeSize[src])
            
            for child in g[src]:
                if child!=par:
                    solve(child,src,ans[src]-(subTreeAns[child]+subTreeSize[child]),total_nodes)
        
        dfs(0,-1)
        solve(0,0,0,n)
        
        return ans
            
            
            