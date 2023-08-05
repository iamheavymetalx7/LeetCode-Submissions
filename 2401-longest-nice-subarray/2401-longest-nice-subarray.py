class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
            l,mask,ans=-1,0,1
            
            
            for r,n in enumerate(nums):
                while mask&n:
                    l+=1
                    mask^=nums[l]
                mask|=n
                ans = max(ans,r-l)
            
            return ans