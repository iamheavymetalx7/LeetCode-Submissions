class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for x,y in paths:
            graph[x-1].append(y-1)
            graph[y-1].append(x-1)
        
                
        
            
        res = [0]*(n)
        
        for i in range(n):
            col = [1,2,3,4]
            
            for ele in graph[i]:
                if res[ele] in col:
                    col.remove(res[ele])
            res[i] = col.pop()
        
        return res
            
        
        