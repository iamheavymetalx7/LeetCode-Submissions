class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if sum(nums)==len(nums):
            return len(nums)-1
        
        n=len(nums)
        
        zero,l,r,ans=0,0,0,0
        
        for r in range(n):
            if nums[r]==0:
                zero+=1
            
            while zero>1:
                if nums[l]==0:
                    zero-=1
                l+=1
            
            ans=max(ans, r-l+1-zero)
        return ans
        