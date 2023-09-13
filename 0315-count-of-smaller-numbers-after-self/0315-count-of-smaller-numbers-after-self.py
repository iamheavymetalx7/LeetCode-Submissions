class BIT:
    def __init__(self,n):
        self.sums=[0]*(n+1)
    
    def update(self,idx,val):
        while idx<len(self.sums):
            self.sums[idx]+=val
            idx+=(idx&(-idx))
            
    def query(self,idx):
        s=0
        while idx>0:
            s+=self.sums[idx]
            idx-=(idx&(-idx))
        
        return s
            
'''
here val =1, this is similar to count inversions questions, 1 since, we just want to count,
so each time we want sum only

'''
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        n=len(set(nums))
        
        dic = {v:i for i,v in enumerate(sorted(set(nums)))}
        
        Fenwick = BIT(n)
        ans = []
        
        for i in reversed(range(len(nums))):
            ans.append(Fenwick.query(dic[nums[i]]))
            Fenwick.update(dic[nums[i]]+1,1)
            
        return ans[::-1]
        