class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n=len(intervals)
        print(intervals)
        cnt=0
        
        end = intervals[0][1]
        
        for i in range(1,n):
            if end<=intervals[i][0]:
                end= intervals[i][1]
            else:
                cnt+=1
                end =min(end, intervals[i][1])
                
        return cnt
                