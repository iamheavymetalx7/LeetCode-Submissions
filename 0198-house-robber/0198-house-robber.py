class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n=len(nums)
        
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def recur(index):
            if index>=n:
                return 0
            

            return max(recur(index+2)+nums[index],recur(index+1))
            
        
        return recur(0)