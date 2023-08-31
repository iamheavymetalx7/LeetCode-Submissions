'''
reference:
https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/3982919/C%2B%2B-oror-DP-(recursion-%2B-memoization)-oror-Day-31
'''
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
            
        intervals= []
        INT_MAX = int(1e19)
        for i in range(len(ranges)):
            left = max(0,i-ranges[i])
            right = min(n,i+ranges[i])
            
            intervals.append([left,right])
        intervals.sort()
        # print(intervals)
        m =len(intervals)
        
        @cache
        def recur(idx):
            if intervals[idx][1]>=n:
                return 1
            
            if idx>=m:
                return INT_MAX
            
            ans = int(1e19)
            
            for j in range(idx+1,m):
                if intervals[j][0]>intervals[idx][1]:
                    break
                ans = min(ans,1+recur(j))
            
            return ans
        
        val = INT_MAX
        for i in range(m):
            if intervals[i][0]==0:
                
                x = recur(i)
                val=min(val,x)
        
        if val==INT_MAX:
            return -1
        return val