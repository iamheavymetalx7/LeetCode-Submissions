from heapq import heappush, heappop, heapify
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        arr=[]
        for i in range(len(tasks)):
            heappush(arr,[tasks[i][0],tasks[i][1],i])
        
        heap=[]
        
        begin,duration,index=heappop(arr)
        end=begin+duration
        res=[index]
        
        while arr or heap:
            
            while arr and arr[0][0]<=end:
                begin,duration,index = heappop(arr)
                heappush(heap,[duration,index,begin])
            
            if not heap:
                begin,duration,index = heappop(arr)
                heappush(heap,[duration,index,begin])
                
            duration,index,begin = heappop(heap)
            res.append(index)
            
            end = max(end+duration,begin+duration)
            
                
        return res