class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        
        graph = defaultdict(list)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    graph[i].append(j)
        
        print(graph)
        
        
        vis=set()
        ans=0
        for i in range(n):
            if i not in vis:
                ans+=1
                q=deque()
                q.append(i)
                vis.add(i)
                
                while q:
                    ele =q.popleft()
                    # print(ele,"elelele")
                    for nei in graph[ele]:
                        if nei not in vis:
                            vis.add(nei)
                            q.append(nei)
        return ans
                        