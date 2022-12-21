class Solution:
    
    def isPossible(self,mid,k,nums):
        total=0
        count=0
        
        for i in range(len(nums)):
            if nums[i]>mid:
                return False
            if total+nums[i]>mid:
                count+=1
                total=nums[i]
            else:
                total+=nums[i]
        
        if count<k:
            return True
        
        return False
        
        
    def splitArray(self, nums: List[int], k: int) -> int:
        low=min(nums)
        high=sum(nums)
        
        if k>len(nums):
            return -1
        
        while low<=high:
            mid=(low+high)//2
            
            if self.isPossible(mid,k,nums):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    
    