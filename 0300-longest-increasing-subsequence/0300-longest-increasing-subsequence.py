class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums) 
        dp=[1]*n
        for index in range(n):
            for prev in range(index):
                if nums[index]>nums[prev]:
                    dp[index]=max(dp[index],1+dp[prev])
        
        return max(dp)
                    
        
                
                
