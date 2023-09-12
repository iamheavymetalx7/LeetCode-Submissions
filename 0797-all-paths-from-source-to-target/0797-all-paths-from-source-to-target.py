class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        vis= [0]*(n)
        
        ans =[]
        
        def dfs(src,arr):
            vis[src]=1
            
            if src==n-1:
                arr.append(src)
                ans.append(arr.copy())
                vis[src]=0
                arr.pop()
                
                                
            
            for nei in graph[src]:
                if not vis[nei]:
                    arr.append(src)
                    dfs(nei,arr)
                    arr.pop()
                    vis[src]=0
                    
        dfs(0,[])
        return ans