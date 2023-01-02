class Solution:
    def search(self, nums: List[int], key: int) -> int:
        low=0
        high=len(nums)-1
        
        while low<=high:
            mid=(low+high)//2
            
            if nums[mid]==key:
                return mid
            
            if nums[low]<=nums[mid]:   ##this implies numbers from start-->mid in ascending order:
                if key>=nums[low] and key<=nums[mid]:
                    high=mid-1
                else:   # key >nums[mid]
                    low=mid+1
            else: #this implies mid->end in ascending order
                if key>=nums[mid] and key<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1
                