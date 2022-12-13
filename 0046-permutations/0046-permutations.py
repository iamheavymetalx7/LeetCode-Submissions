class Solution:
    def recur(self,index,nums,ans):
        if index==len(nums):
            ans.append(nums.copy())
            return
        
        for i in range(index,len(nums)):
            nums[index],nums[i]=nums[i],nums[index]
            self.recur(index+1,nums,ans)
            nums[index],nums[i]=nums[i],nums[index]
    
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        self.recur(0,nums,ans)
        return ans
        
        
        
        
        
        
        
        
        
        
'''
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

'''