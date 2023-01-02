class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        three_sum = sum(set(nums))*3
        
        one_sum = sum(nums)
        
        rem = three_sum-one_sum
        
        return rem//2