class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n=len(nums)
        
        @cache
        def recur(idx,prev):
            if idx>=n:
                return 0
            ans =0
            for j in range(idx,n):
                if nums[j]>prev:
                    ans = max(ans,1+recur(j+1,nums[j]))
            
            return ans
        
        val = recur(0,-int(1e19))
        return val
                    