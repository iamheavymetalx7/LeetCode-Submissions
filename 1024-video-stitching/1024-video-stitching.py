'''
this approach is taken using the help of  https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/submissions/
'''
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()

        int_max = int(1e19)
        n=len(clips)
        
        @cache
        def recur(idx):
            if clips[idx][1]>=time:
                return 1
            if idx>=n:
                return int_max
            ans = int_max
            for j in range(idx+1,n):
                if clips[j][0]>clips[idx][1]:
                    break
                ans = min(ans,1+recur(j))
            return ans
        
        val = int_max
        
        for i in range(n):
            if clips[i][0]==0:
                val = min(val, recur(i))
        
        return val if val!=int_max else -1
                