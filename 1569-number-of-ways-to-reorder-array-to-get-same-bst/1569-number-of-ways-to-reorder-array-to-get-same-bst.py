from math import comb


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        
        def calc(nums):
            if len(nums)<=2:
                return 1
            
            less = [v for v in nums if v<nums[0]]
            more = [v for v in nums if v>nums[0]]
            
            return comb(len(less)+len(more), len(less))*calc(less)*calc(more)
        
        ans = calc(nums)
        return (ans-1)%(10**9+7)
        

            
            
                
        
            
        
        
        