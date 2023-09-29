class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        def monotonic(nums):
            f= True
            for i in range(len(nums)-1):
                if nums[i]>=nums[i+1]:
                    continue
                else:
                    return False

            return True
        
        
        return monotonic(nums) or monotonic(nums[::-1])
            