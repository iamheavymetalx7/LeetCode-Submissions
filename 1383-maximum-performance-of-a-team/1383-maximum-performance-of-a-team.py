from heapq import heapify, heappush, heappop
class Solution:
    def maxPerformance(self, n: int, speed: List[int], eff: List[int], k: int) -> int:
        # same as https://leetcode.com/contest/biweekly-contest-96/problems/maximum-subsequence-score/
        
        # minimum - efficiencyy
        # sum of engineer's speeds
        
        mod = 10**9+7
        
        pq=[]
        total=0
        res=-1
        for b,a in sorted(zip(eff,speed),key=lambda x:-x[0]):
            heappush(pq,a)
            total+=a
            
            if len(pq)>k:
                total-=heappop(pq)

            res=max(res,total*b)
                            
        return res%mod
        
        