class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        tree=[[] for _ in range(n)]
        
        for x,y in connections:
            tree[x].append((y,1))
            tree[y].append((x,0))
        
        vis = set()
        ans=0
        
        def dfs(src,par):
            nonlocal ans
            
            for nei,val in tree[src]:
                if nei==par:
                    continue
                ans+=val
                dfs(nei,src)
                
        
        dfs(0,-1)
        return ans
                
                    
                
            