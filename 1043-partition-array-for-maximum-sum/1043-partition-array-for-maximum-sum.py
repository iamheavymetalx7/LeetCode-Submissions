import math
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp=[-1]*n
        def recur(index):
            if index==n:
                return 0
            
            if dp[index]!=-1:
                return dp[index]
            length=0
            maxi=-math.inf
            summ_maxi =-math.inf
            for j in range(index, min(n,index+k)):
                length+=1
                maxi=max(maxi,arr[j])
                
                summ=maxi*length + recur(j+1)
                
                summ_maxi = max(summ_maxi, summ)
            dp[index] = summ_maxi
            return dp[index]
        return recur(0)
                
                
        