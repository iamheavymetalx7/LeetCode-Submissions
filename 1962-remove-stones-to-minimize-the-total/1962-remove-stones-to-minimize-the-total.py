from heapq import heapify, heappush, heappop
import math
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        pq=[]
        
        for st in piles:
            heappush(pq,-st)
        # print(pq)
        for i in range(k):
            top_ele = heappop(pq)
            top_ele=-1*top_ele
            sub_val = math.floor(top_ele/2)
            new_val = top_ele - sub_val
            heappush(pq, -new_val)
            
        return(-1*sum(pq))