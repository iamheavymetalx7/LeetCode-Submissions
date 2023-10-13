class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        
        heap =[]
        for i in range(n):
            for j in range(i+1,n):
                heappush(heap,[arr[i]/arr[j],[arr[i],arr[j]]])
        
        for i in range(k-1):
            heappop(heap)
        
        a,b = heappop(heap)
        return b