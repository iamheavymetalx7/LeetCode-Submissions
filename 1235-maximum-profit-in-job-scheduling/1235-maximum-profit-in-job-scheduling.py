'''
optimized using binary search and take-nottake cases
'''
from bisect import bisect_left as lb
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        jobs = []
        
        n = len(profit)
        
        for i in range(n):
            jobs.append([startTime[i],endTime[i],profit[i]])
        
        jobs.sort()
        startTime.sort()
        
        @cache
        def recur(idx):
            if idx>=n:
                return 0
            
            ans =0
            # if we are taking, we need to find the next index to which we go
            newidx = lb(startTime, jobs[idx][1])
            
            #take, take into acc the profit
            ans = max(ans, recur(newidx)+jobs[idx][2])
            
            #nottake, no need to add anything
            ans = max(ans, recur(idx+1))
            
            return ans
        
        val = recur(0)
        
        return val