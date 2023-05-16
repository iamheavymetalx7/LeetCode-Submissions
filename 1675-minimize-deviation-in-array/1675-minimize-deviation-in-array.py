from heapq import *
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq=[-2*x if x&1 else -x for x in nums]
        
        heapify(pq)
        
        maxi=max(pq)
        
        ans=maxi-pq[0]
        
        while pq[0]%2==0:
            top = heappop(pq)
            top = top//2
            heappush(pq,top)
            maxi=max(maxi,top)
            
            ans=min(ans, maxi-pq[0])
        
        return ans