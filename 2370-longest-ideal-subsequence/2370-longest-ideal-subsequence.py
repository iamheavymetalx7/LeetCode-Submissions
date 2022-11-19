class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp=[0]*26
        n=len(s)
        
        for char in s:
            x=ord(char)-ord('a')
            val=0
            lb=max(0,x-k)
            ub=min(25,x+k)
            for i in range(lb,ub+1):
                val=max(val,dp[i])
            dp[x]=val+1
            
        ans=max(dp)
        return ans
        