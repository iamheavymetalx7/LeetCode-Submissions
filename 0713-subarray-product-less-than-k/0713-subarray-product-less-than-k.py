class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left=0
        pdt=1
        res=0
        
        for right in range(len(nums)):
            pdt*=nums[right]
            
            while pdt>=k and left<right:
                pdt/=nums[left]
                left+=1
            
            if pdt<k:
                res+=right-left+1
        return res
            
            