class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        vis=[0]*len(graph)
        ans=[]
        
        def dfs(node,arr):
            vis[node]=1

            if node==len(graph)-1:
                arr.append(node)
                vis[node]=0
                ans.append(arr)
                
            
            
            for j in graph[node]:
                if not vis[j]:
                    dfs(j,arr+[node])
                    vis[node]=0
                    
                    
        dfs(0,[])
        
        return ans
            
        