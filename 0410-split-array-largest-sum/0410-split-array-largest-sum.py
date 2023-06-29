class Solution:

    def isPossible(self,m,nums,k):
        n=len(nums)
        cnt=1
        summ=0
        for i in range(len(nums)):
            summ+=nums[i]
            if nums[i]>m:
                return False
            if summ>m:
                # print(m,summ)
                cnt+=1
                summ=nums[i]
        return cnt<=k
    
    
    def splitArray(self, nums: List[int], k: int) -> int:
        
        l=max(nums)-1;r=sum(nums)+1
        
        while r>l+1:
            m=(l+r)//2
            if self.isPossible(m,nums,k):
                r=m
            else:
                l=m
        return r