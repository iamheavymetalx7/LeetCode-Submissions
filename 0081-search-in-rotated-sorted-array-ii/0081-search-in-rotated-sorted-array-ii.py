class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        l=0
        r=n-1
        
        while l<=r:
            mid = (l+r)//2
            
            if nums[mid]==target:
                return True
            
            if nums[mid]==nums[l] and nums[mid]==nums[r]:
                l+=1
                r-=1

            elif nums[l]<=nums[mid]:  ## this part is sorted:
                if nums[l]<=target<=nums[mid]:

                    r=mid-1
                
                else:
                    l=mid+1
            else:
                if nums[mid]<=target<=nums[r]:

                    l=mid+1
                
                else:
                    r=mid-1
        return False