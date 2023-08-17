class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        l=0
        ans =0
        n=len(nums)
        for r in range(n):
            
            if nums[r]==0:
                k-=1
            
            while k<0:
                ans=max(ans,r-l)
                
                if nums[l]==0:
                    k+=1
                l+=1
        ans=max(ans,r-l+1)
        return ans
                
                