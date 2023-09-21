class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        
        s=0
        left=0
        maxheap =[]
        res=0
        n=len(runningCosts)
        for right in range(n):
            s+=runningCosts[right]
            heappush(maxheap,[-chargeTimes[right],right])
            
            while maxheap and (-maxheap[0][0])+s*(right-left+1)>budget:
                s-=runningCosts[left]
                
                while maxheap and maxheap[0][1]<=left:
                    heappop(maxheap)
                left+=1

                    
            res = max(res,right-left+1)
        return res