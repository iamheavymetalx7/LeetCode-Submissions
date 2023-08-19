class Solution:
    def minRefuelStops(self, tgt: int, tank: int, stations: List[List[int]]) -> int:
        
        ans=0
        prev = 0
        stations.append([tgt,int(1e19)])
        maxheap=[]
        
        for pos,fuel in stations:
            
            tank -= pos-prev
            # print(tank,pos,fuel)
            
            while tank<0 and maxheap:
                ans+=1
                tank+=-heappop(maxheap)
            
            if tank<0:
                return -1
            
            heappush(maxheap,-fuel)
            prev=pos
        return ans
            
            

        