from heapq import heappush, heapify, heappop
class Solution:
    def findScore(self, nums: List[int]) -> int:
        pq=[]
        n=len(nums)
        seen=set()
        for i in range(len(nums)):
            heappush(pq,[nums[i],i])
        score=0
        while pq:
            ele,idx = heappop(pq)
            
            if (ele,idx) in seen:
                continue
                
            seen.add((ele,idx))
            
            
            score+=ele

            seen.add((nums[min(idx+1,n-1)],min(idx+1,n-1)))
            seen.add((nums[max(idx-1,0)],max(idx-1,0)))
        return score
                
        
        