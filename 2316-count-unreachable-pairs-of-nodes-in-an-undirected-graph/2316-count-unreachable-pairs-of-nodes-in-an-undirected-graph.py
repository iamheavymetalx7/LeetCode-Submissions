class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        vis=set()
        
        graph=collections.defaultdict(list)
        
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(u):
            nonlocal cnt_of_ele

            if u in vis:
                return
            cnt_of_ele+=1
            vis.add(u)
            
            for v in graph[u]:
                if v not in vis:
                    dfs(v)
        
        res=0
        for i in range(n):
            if i not in vis:
                cnt_of_ele = 0
                dfs(i)
                res+= (cnt_of_ele)*(n-cnt_of_ele)   
        
        return res//2