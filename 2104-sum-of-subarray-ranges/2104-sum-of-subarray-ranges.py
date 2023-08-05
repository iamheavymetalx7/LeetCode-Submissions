class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n =len(nums)
        
        ans =0
        for i in range(n):
            l,r = nums[i],nums[i]

            for j in range(i,n):
                l=min(l,nums[j])
                r=max(r,nums[j])
                
                ans+=(r-l)
                
                
        return ans