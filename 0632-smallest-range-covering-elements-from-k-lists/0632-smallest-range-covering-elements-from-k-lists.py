from heapq import *
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq=[]
        rangeStart, rangeEnd=0,math.inf
        currentMax = -math.inf
        for arr in nums:
            heappush(pq,(arr[0],0,arr))
            currentMax = max(currentMax, arr[0])
        
        while len(nums)==len(pq):
            num,i,lst=heappop(pq)
            
            if rangeEnd-rangeStart > currentMax-num:
                rangeStart, rangeEnd=num,currentMax
            
            if len(lst)>i+1:
                heappush(pq,(lst[i+1],i+1,lst))
                currentMax=max(currentMax, lst[i+1])
        
        return [rangeStart,rangeEnd]