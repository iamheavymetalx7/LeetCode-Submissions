class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        o=0
        for x in nums:
            o|=x
        
        return o*pow(2,len(nums)-1)