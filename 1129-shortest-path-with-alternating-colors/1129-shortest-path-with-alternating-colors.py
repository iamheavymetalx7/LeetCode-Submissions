class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        red = defaultdict(list)
        blue=defaultdict(list)
        
        for src, dst in redEdges:
            red[src].append(dst)
            
            
        for src, dst in blueEdges:
            blue[src].append(dst)
        
        
        ans=[-1 for _ in range(n)]
        
        q=deque()
        q.append([0,0,None]) ## this is node, length, color
        
        vis=set()
        
        vis.add((0,None))
        
        
        while q:
            node, length, edgeC = q.popleft()
            
            if ans[node]==-1:
                ans[node] = length
            
            if edgeC!="RED":
                for nei in red[node]:
                    if (nei, "RED") not in vis:
                        q.append([nei, length+1, "RED"])
                        vis.add((nei,"RED"))

            if edgeC!="BLUE":
                for nei in blue[node]:
                    if (nei, "BLUE") not in vis:
                        q.append([nei, length+1, "BLUE"])
                        vis.add((nei,"BLUE"))
        
        return ans
        