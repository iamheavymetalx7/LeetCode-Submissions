from collections import defaultdict
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        visited= [False]*n
        
        adj=defaultdict(list)
        
        for j in range(len(rooms)):
            adj[j]=rooms[j]
        
        def dfs(node):
            visited[node]=True
        
            for ele in adj[node]:
                if not visited[ele]:
                    dfs(ele)
        dfs(0)
        
        return (all(visited))                
            