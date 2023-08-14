class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap=[]
        for x in nums:
            heappush(heap,-int(x))
        
        for x in range(k-1):
            heappop(heap)
        return str(-heap[0])