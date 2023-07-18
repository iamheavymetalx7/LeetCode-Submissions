class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        
        dic = defaultdict(list)
        for x,y in roads:
            dic[x].append(y)
            dic[y].append(x)
        
        
        def dfs(node,parent):
            nonlocal res
            ppl =0
            
            for ele in dic[node]:
                if ele!=parent:
                    p=dfs(ele,node)
                    ppl+=p
                    res+=(p+seats-1)//(seats)
            return ppl+1
        
        
        res =0
        dfs(0,-1)
        
        
        return res
        
                    
            
            