## choosing the correct left boundary in this case is important!!
## moreove the boolean condition should be set to s<=k and not s==k
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        
        if k==1:
            return sum(nums)
        
        
        def check(x,k):
            s=1
            tot=0
            n=len(nums)
            for i in range(n):
                if tot+nums[i]>x:
                    tot=nums[i]
                    s+=1
                else:
                    tot+=nums[i]
            if s<=k:
                return True
            
            return False
        
        l=max(nums)-1
        r=sum(nums)+1
        
        
        
        
        while r>l+1:
            m=(l+r)//2
            
            if check(m,k):
                r=m
            else:
                l=m

        return r