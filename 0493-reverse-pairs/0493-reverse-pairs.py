class BIT:
    def __init__(self,n):
        self.sums =[0]*(n+1)
    
    def query(self,idx):
        res = 0
        while idx>0:
            res+=self.sums[idx]
            idx-=(idx&(-idx))
        return res
    
    def update(self,idx,val):
        
        while idx<len(self.sums):
            self.sums[idx]+=val
            idx+=(idx&(-idx))
    
            
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        new_nums = nums+[2*n for n in nums]
        
        dic= {v:i for i,v in enumerate(sorted(set(new_nums)))}
        
        Fenwick = BIT(len(dic))
        res=0
        
        for i in reversed(range(len(nums))):
            res+=Fenwick.query(dic[nums[i]])
            Fenwick.update(dic[2*nums[i]]+1,1)
        
        return res