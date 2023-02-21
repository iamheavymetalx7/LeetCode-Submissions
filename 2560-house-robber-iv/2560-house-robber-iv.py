class Solution:
    def isPossible(self,m,nums,k):
        prev_index=-10**9
        cnt=0
        for idx in range(len(nums)):
            if nums[idx]>m:
                continue
            if idx==prev_index+1:
                continue
            cnt+=1
            prev_index=idx
            if cnt>=k:
                return True
        return False
            
            
        
    
    def minCapability(self, nums: List[int], k: int) -> int:
        l=1
        r=max(nums)        
        while r>l:
            m=(l+r)//2
            print(l,r)
            if self.isPossible(m,nums,k):
                r=m
            else:
                l=m+1
        return l
        