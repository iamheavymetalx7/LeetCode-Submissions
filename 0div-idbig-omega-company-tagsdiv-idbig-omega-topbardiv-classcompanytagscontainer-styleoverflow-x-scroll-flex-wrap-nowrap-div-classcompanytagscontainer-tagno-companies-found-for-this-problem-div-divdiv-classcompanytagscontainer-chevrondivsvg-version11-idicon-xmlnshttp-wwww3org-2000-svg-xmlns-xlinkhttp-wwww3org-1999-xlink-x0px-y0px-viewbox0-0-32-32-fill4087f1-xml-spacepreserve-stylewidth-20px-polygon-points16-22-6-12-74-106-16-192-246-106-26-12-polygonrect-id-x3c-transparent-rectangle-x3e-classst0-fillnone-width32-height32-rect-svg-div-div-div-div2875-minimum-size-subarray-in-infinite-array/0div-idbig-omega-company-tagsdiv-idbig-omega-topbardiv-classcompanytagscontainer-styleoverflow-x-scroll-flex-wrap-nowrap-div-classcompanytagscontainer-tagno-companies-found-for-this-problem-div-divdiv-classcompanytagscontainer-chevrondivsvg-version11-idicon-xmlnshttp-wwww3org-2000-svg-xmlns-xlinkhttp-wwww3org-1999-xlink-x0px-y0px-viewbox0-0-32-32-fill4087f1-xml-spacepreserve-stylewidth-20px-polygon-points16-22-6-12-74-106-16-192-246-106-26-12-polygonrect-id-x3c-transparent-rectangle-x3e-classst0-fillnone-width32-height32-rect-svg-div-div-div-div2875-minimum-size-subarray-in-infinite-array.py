class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        
        summ=sum(nums)
        
        newtarget = target%summ
        howmany = target//summ
        
        n=len(nums)
        new_nums = nums+nums
        m=len(new_nums)
        l=0
        curr=0
        reqd = int(1e19)
        for r in range(m):
            curr+=new_nums[r]
            
            while curr>newtarget:
                curr-=new_nums[l]
                l+=1
            if curr==newtarget:
                reqd = min(reqd,r-l+1)
        
        if reqd == int(1e19):return -1
        
        return reqd+howmany*n
                
            
            
            