class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        
        if n%2:
            val = nums[n//2]
        else:
            val =(nums[n//2]+nums[(n-2)//2]) //2
        tot=0
        for x in nums:
            tot+=abs(x-val)
        return tot
            