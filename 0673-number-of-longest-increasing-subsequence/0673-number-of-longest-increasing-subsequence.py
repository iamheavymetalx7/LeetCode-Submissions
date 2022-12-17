class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        cnt=[1]*n
        
        maxi=1
        for i in range(n):
            for prev in range(i):
                if nums[prev]<nums[i] and dp[i]<dp[prev]+1:
                    dp[i]=dp[prev]+1
                    cnt[i]=cnt[prev]
                elif nums[prev]<nums[i] and dp[i]==dp[prev]+1:
                    cnt[i]+=cnt[prev]
        
            if maxi<dp[i]:
                maxi=dp[i]
                
                
        nos=0
        for i in range(n):
            if dp[i]==maxi:
                nos+=cnt[i]
                
        return nos