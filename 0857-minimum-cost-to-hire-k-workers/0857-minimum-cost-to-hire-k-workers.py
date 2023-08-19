from fractions import Fraction
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        arr=[]
        
        arr=[(Fraction(w,q),q,w) for (q,w) in zip(quality,wage)]
        arr.sort()
        
        heap =[]
        sumq=0
        ans=int(1e19)
        
        for ratio,q,w in arr:
            heappush(heap,-q)
            
            sumq+=q
            
            if len(heap)>k:
                sumq+=heappop(heap)
            
            if len(heap)==k:
                ans=min(ans,sumq*ratio)
        return ans