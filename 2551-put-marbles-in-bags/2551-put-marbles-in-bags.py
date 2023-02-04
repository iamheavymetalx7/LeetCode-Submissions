class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        if k==len(weights):
            return 0
        
        paritionWeights = [weights[i]+weights[i-1] for i in range(1,len(weights))]
        

        return sum(heapq.nlargest(k-1, paritionWeights))-sum(heapq.nsmallest(k-1,paritionWeights))