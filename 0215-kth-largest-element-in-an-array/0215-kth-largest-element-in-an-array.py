class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap =[]
        
        for x in nums:
            heappush(heap,-x)
        
        for _ in range(k-1):
            heappop(heap)
        
        ans = -heappop(heap)
        return ans