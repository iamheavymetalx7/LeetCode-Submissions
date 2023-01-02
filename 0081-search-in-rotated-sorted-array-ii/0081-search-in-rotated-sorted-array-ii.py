class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low,high=0,len(nums)-1
        
        while low<=high:
            mid=(low+high)//2
            
            if nums[mid]==target:
                return True
                # return the index
            
            
            if nums[mid]==nums[low] and nums[mid]==nums[high]:
                low+=1
                high-=1
            elif nums[low]<=nums[mid]:   #left side sorted
                if target>=nums[low] and target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if target>=nums[mid] and target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return False