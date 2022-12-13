class Solution:
    
    def recursion(self,idx,nums,ans,ds):
        ans.append(ds)
        for i in range(idx,len(nums)):
            if i>idx and nums[i]==nums[i-1]:
                continue
            self.recursion(i+1,nums,ans,ds+[nums[i]])
    
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        ds=[]
        nums.sort()
        self.recursion(0,nums,ans,ds)
        return ans
        