class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        
        if nums==[1]*n:
            return n-1
        
        dp=[[0]*2 for _ in range(n)]
        
        dp[0][0] = nums[0]
        
        for idx in range(1,n):
            if nums[idx]==1:
                dp[idx][0] = 1+dp[idx-1][0]
                dp[idx][1] = 1+dp[idx-1][1]
            
            else:
                dp[idx][0]=0
                dp[idx][1] = dp[idx-1][0]
        
        ans=0
        for x in range(n):
            for y in range(2):
                ans=max(ans, dp[x][y])
        
        return ans
            
                
        