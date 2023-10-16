class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = int(1e9)+7
        @cache
        def recur(idx,rem):

            if rem==0:
                if idx==0:
                    return 1
                return 0
            
            ans = 0
            ans = (ans+recur(idx,rem-1))%mod
            if idx>0:
                ans = (ans+recur(idx-1,rem-1))%mod
            if idx<arrLen-1:
                ans  =(ans+recur(idx+1,rem-1))%mod
            return ans
        
        val = recur(0,steps)
        return val%mod