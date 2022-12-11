from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq=[]
        for i in range(min(k,len(matrix))):
            heappush(pq,(matrix[i][0],0,matrix[i]))
        
        cnt, number =0,0
        
        while pq:
            number, i, lst = heappop(pq)
            
            cnt+=1
            if cnt==k:
                break
            
            if len(lst)>i+1:
                heappush(pq,(lst[i+1],i+1,lst))
                
        return number