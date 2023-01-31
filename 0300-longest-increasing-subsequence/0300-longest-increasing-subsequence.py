class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        
        dp=[[0]*(n+1) for _ in range(n+1)]
        
        for index in range(n-1,-1,-1):
            for prev_ind in range(index-1,-2,-1):
                
                length=dp[index+1][prev_ind+1]
                
                if prev_ind==-1 or nums[index]>nums[prev_ind]:
                    length=max(length,1+dp[index+1][index+1])
                
                dp[index][prev_ind+1]=length
                
        return dp[0][-1+1]            
        
                
                
