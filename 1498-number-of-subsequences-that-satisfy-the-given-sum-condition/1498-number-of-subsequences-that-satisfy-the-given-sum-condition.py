class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod=10**9+7
        res=0
        pointer = len(nums)-1
        
        for i,left in enumerate(nums):
            while left+nums[pointer]>target and i<=pointer:
                pointer-=1
            if i<=pointer:
                res+=pow(2,pointer-i,mod)
        return res%mod
                
                
        