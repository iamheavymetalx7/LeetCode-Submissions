class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for x,y in paths:
            x-=1
            y-=1
            graph[x].append(y)
            graph[y].append(x)
        
        
        res =[0]*(n)
        
        for i in range(n):
            col =[1,2,3,4]
            
            for nei in graph[i]:
                if res[nei] in col:
                    col.remove(res[nei])
            res[i]=col.pop()
        return res
                
        