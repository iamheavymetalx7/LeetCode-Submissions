class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_sum=nums[0]
        cur_sum=nums[0]
        n=len(nums)
        
        for i in range(1,n):
            cur_sum=max(nums[i],nums[i]+cur_sum)
            max_sum=max(max_sum,cur_sum)
        
        return max_sum
        