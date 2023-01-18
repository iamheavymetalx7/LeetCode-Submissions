class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
    
        ## kadane's algo
        
        if max(nums)<=0:
            return max(nums)

        cur_max=nums[0]
        cur_min=nums[0]
        max_sum=nums[0]
        min_sum=nums[0]
        
        for num in nums[1:]:
            cur_max = max(num, cur_max+num)
            max_sum = max(cur_max, max_sum)
            cur_min = min(num, cur_min+num)
            min_sum = min(min_sum, cur_min)
            
        return max(max_sum,sum(nums)-min_sum)
        