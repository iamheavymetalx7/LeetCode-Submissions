class BIT:
    def __init__(self,n):
        self.sums=[0]*(n+1)
    
    def update(self,idx,val):
        while idx<len(self.sums):

            self.sums[idx]=max(val,self.sums[idx])
            idx+=(idx&(-idx))
            
    def query(self,idx):
        s=0
        while idx>0:
            s=max(self.sums[idx],s)
            idx-=(idx&(-idx))
        
        return s

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dic={v:i for i,v in enumerate(sorted(set(nums)))}
        
        Fenwick = BIT(len(dic))
        
        n=len(nums)
        
        res= 0
        
        for i in range(n):
            lis = Fenwick.query(dic[nums[i]])
            lis+=1
            res=max(res,lis)
            
            Fenwick.update(dic[nums[i]]+1,lis)
        
        return res
        
        