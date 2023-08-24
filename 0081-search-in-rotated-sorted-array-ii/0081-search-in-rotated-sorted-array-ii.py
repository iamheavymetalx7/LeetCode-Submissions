class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        r=len(nums)-1
        n=len(nums)
        
        # [1,0,1]
        #  0 1 2 3 4 5 6
        
        while l<=r:


            mid = (l+r)//2
            
            if nums[mid]==target:
                return True
            
                
            while l<r and nums[mid]==nums[l]==nums[r]:
                l+=1
                r-=1
            # print(mid,"mid",l,r)

            
            if nums[mid]<=nums[r]:
                if nums[mid]<=target<=nums[r]:
                    l = mid+1
                else:
                    r=mid-1

            elif nums[l]<=nums[mid]:
                if nums[l]<=target<=nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
        return False
        
                    