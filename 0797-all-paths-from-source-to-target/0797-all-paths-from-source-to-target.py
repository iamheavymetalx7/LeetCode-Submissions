class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        vis=[0]*len(graph)
        ans=[]
        n=len(graph)
        
        def dfs(node,arr):
            vis[node]=1

            if node==n-1:
                arr.append(node)
                ans.append(arr)
                vis[node]=0
                
            
            
            for nei in graph[node]:
                if not vis[nei]:
                    dfs(nei,arr+[node])
                    vis[node]=0
                    
                    
        dfs(0,[])
        
        return ans