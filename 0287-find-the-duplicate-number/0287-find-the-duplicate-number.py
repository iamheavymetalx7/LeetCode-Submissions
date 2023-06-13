class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     idx = abs(nums[i])-1
        #     if nums[idx]>0:
        #         nums[idx]*=-1
        #     else:
        #         return idx+1
        i=0
        n=len(nums)
        while i<n:
            correct  = nums[i]-1
            if nums[i]!=nums[correct]:
                nums[i],nums[correct] = nums[correct],nums[i]
            else:
                i+=1
        for i in range(n):
            if nums[i]!=(i+1):
                return nums[i]
            
            