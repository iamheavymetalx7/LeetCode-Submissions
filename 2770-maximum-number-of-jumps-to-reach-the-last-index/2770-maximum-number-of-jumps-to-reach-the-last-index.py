class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n=len(nums)
        MIN_INF = -10**9
        dp=[-1]*(n)
        
        def recur(idx):
            if idx==n-1:
                return 0
            
            if dp[idx]!=-1:
                return dp[idx]
            
            ans = MIN_INF
            for j in range(idx+1,n):
                if abs(nums[j]-nums[idx])<=target:
                    ans = max(ans,1+recur(j))
            
            dp[idx]=ans
            return dp[idx]
        
        ans =  recur(0)
        if ans<0:
            return -1
        return ans
            