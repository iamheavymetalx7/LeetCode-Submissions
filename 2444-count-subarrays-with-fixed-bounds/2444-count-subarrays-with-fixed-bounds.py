class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        bad_i=-1
        max_i=-1
        min_i=-1
        
        n=len(nums)
        
        ans=0
        
        for i in range(n):
            if nums[i]<minK or nums[i]>maxK:
                bad_i=i 
            if nums[i]==minK:
                min_i=i
            if nums[i]==maxK:
                max_i=i
            # print(min_i,max_i,bad_i)
            
            ans+=max(0,min(max_i,min_i)-bad_i)
        return ans