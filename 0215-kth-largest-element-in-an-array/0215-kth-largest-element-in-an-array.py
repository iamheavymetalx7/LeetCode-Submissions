class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        pq=[]
        
        for x in nums:
            heappush(pq,-x)
        
        
        for j in range(k):
            ele = heappop(pq)
        
        return(-1*ele)