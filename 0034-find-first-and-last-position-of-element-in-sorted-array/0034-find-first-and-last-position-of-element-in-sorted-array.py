class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        final_ans=[-1,-1]
        
        
        
        def search(low,high,firstIndex):
            ans=-1
            while low<=high:
                mid=(low+high)//2
                
                if nums[mid]>target:
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    ans=mid
                    if firstIndex:
                        high=mid-1
                    else:
                        low=mid+1
            return ans
        
        final_ans[0] = search(0,len(nums)-1, True)
        final_ans[1] = search(0,len(nums)-1, False)
        
        return final_ans