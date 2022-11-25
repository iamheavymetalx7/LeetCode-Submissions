class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms=[]
        
        if len(nums)==1:
            return [nums[:]]
        
        for i in range(len(nums)):
            for l in self.permute(nums[:i]+nums[i+1:]):
                perms.append([nums[i]]+l)
        
        return perms
        