class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n=len(events)
        
        events.sort()

        start = [s for s, e, v in events]
        end = [e for s, e, v in events]
        values = [v for s, e, v in events]
        
        max_on_right=[-1]*(n)
        
        max_on_right[n-1]=events[n-1][2]
        
        for idx in range(n-1)[::-1]:
            max_on_right[idx]=max(events[idx][2],max_on_right[idx+1])
            
        res=max(values)        
        for i in range(n):
            curr = values[i]
            
            idx = bisect.bisect_right(start,end[i])
            if idx==n:
                continue
            res=max(res,curr+max_on_right[idx])
        return res
                    
                    
            