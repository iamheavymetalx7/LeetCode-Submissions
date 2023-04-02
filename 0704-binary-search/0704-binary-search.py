class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=-1
        r=len(nums)+1
        
        if target<nums[0] or target>nums[-1]:
            return -1
        
        while r>l+1:
            m=(l+r)//2
            # print(m)
            
            if nums[m]==target:
                return m
            elif nums[m]>target:
                r=m
            else:
                l=m
        return -1
                
                