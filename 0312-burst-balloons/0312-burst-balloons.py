class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums=[1]+nums+[1]
        
        n=len(nums)
    
        @cache
        def dp(i,j):
            if i>j:
                return 0
            ans=0
            for k in range(i,j+1):
                coins=nums[i-1]*nums[k]*nums[j+1]
                coins+=dp(i,k-1)+dp(k+1,j)
            
                ans=max(ans,coins)
            return ans
        
        return dp(1,n-2)