import heapq
from heapq import heappush, heappop, heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq=[]
        for i in range(len(nums)):
            heappush(pq,-nums[i])
        
        for j in range(k-1):
            heappop(pq)
            
        return -pq[0]
            
            
            
            
            