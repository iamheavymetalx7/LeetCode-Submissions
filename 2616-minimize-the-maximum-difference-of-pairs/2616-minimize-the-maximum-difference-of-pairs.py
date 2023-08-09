class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        
        l=-1
        r=max(nums)-min(nums)
        
        n=len(nums)
        
        nums.sort()
        
        
        def isPossible(xx):
            i=0
            cnt=0
            
            while i+1<n:
                if nums[i+1]-nums[i]<=xx:
                    i+=1
                    cnt+=1
                i+=1
            if cnt>=p:
                return True
            return False
            
            
            
            
        
        
        while r-l>1:
            mid = (l+r)//2
            
            if isPossible(mid):
                r=mid
            else:
                l=mid
        return r