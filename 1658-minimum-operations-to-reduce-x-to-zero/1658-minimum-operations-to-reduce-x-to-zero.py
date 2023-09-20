class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        l=0
        r=0
        n=len(nums)
        summ=0
        ans=-1
        tgt = sum(nums)-x
        
        for r in range(n):
            summ+=nums[r]
            
            while l<n and summ>tgt:
                summ-=nums[l]
                l+=1
            if summ==tgt:
                ans=max(ans,r-l+1)
        return n-ans if ans!=-1 else -1
            
        