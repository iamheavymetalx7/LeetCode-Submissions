class Solution:
    def countSubarrays(self, A: List[int], k: int) -> int:
        
        res,cur,i=0,0,0
        n=len(A)
        
        for j in range(n):
            cur+=A[j]
            
            while (cur*(j-i+1)>=k):
                cur-=A[i]
                i+=1
            
            res+=(j-i+1)
        return res