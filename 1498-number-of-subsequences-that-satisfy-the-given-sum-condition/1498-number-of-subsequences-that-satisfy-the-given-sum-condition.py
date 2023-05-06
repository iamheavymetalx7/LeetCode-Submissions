class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        mod = 10**9+7
        
        right=len(nums)-1
        
        ans=0
        
        for left in range(len(nums)):
            while nums[left]+nums[right]>target and left<=right:
                right-=1
            if left<=right:
                ans+=pow(2,right-left, mod)
        
        return ans%mod
                
        