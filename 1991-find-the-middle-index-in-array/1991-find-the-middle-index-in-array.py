class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        
        leftsum=0
        rightsum=total
        
        for i in range(len(nums)):
            rightsum-=nums[i]
            if leftsum==rightsum:
                return i
            leftsum+=nums[i]
        return -1
            