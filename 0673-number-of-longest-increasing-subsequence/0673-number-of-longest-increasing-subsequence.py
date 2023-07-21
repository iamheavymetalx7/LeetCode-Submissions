class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp = [1]*(n)
        cnt=[1]*(n)
        for i in range(n):
            for prev in range(i):
                if nums[i]>nums[prev] and dp[i]<1+dp[prev]:
                    dp[i]=1+dp[prev]
                    cnt[i]=cnt[prev]
                elif nums[i]>nums[prev] and dp[i]==1+dp[prev]:
                    cnt[i]+=cnt[prev]
        
        
        maxi = max(dp)
        
        no =0
        for i,x in enumerate(dp):
            if x==maxi:
                no+=cnt[i]
        
        return no