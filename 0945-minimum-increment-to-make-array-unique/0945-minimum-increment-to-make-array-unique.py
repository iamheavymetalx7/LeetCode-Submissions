class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        
        level,res=-1,0
        
        for x in nums:
            if level<x:
                level=x
            else:
                level+=1
                res+=level-x
        return res