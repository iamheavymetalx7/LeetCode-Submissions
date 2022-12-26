class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ans=False
        maxi=nums[0]+0
        n=len(nums)
        for i in range(len(nums)):
            
            if i>maxi:
                return False
            maxi=max(i+nums[i],maxi)

        return True