class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n=len(nums)
        
        
        maxSumm = nums[0]
        currSumm = nums[0]
        
        for i in range(1,n):
            currSumm = max(currSumm+nums[i],nums[i])
            maxSumm= max(maxSumm, currSumm)
        
        return maxSumm