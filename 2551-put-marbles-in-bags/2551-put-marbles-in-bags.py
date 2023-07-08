class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        n=len(weights)
        if k==n:
            return 0
        
        arr=[weights[i+1]+weights[i] for i in range(n-1)]
        
        return sum(heapq.nlargest(k-1, arr))-sum(heapq.nsmallest(k-1,arr))