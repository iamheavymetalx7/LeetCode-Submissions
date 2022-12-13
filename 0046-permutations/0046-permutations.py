from collections import defaultdict
class Solution:
    def recursion(self,ans,ds,nums,freq):
        if len(ds)==len(nums):
            ans.append(ds.copy())
            return
        for i in range(len(nums)):
            if not freq[i]:
                ds.append(nums[i])
                freq[i]=1
                self.recursion(ans,ds,nums,freq)
                freq[i]=0
                ds.pop()
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        ds=[]
        freq=[0]*len(nums)
        self.recursion(ans,ds,nums,freq)
        return ans
        
        