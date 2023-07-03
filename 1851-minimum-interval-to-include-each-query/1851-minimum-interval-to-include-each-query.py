from heapq import *
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = sorted(intervals,reverse=True)
        # print(intervals)
        
        queries = sorted(enumerate(queries),key=lambda x:x[1])
        n=len(queries)
        ans =[-1]*(n)
        
        pq=[]
        
        
        for idx,point in queries:
            
            while pq and pq[0][1]<point:
                heappop(pq)
            
            while intervals and intervals[-1][0]<=point:
                l,r = intervals.pop()
                if r>=point:
                    heappush(pq,(r-l+1,r))
            if pq:
                ans[idx]=pq[0][0]
        return ans
        
        