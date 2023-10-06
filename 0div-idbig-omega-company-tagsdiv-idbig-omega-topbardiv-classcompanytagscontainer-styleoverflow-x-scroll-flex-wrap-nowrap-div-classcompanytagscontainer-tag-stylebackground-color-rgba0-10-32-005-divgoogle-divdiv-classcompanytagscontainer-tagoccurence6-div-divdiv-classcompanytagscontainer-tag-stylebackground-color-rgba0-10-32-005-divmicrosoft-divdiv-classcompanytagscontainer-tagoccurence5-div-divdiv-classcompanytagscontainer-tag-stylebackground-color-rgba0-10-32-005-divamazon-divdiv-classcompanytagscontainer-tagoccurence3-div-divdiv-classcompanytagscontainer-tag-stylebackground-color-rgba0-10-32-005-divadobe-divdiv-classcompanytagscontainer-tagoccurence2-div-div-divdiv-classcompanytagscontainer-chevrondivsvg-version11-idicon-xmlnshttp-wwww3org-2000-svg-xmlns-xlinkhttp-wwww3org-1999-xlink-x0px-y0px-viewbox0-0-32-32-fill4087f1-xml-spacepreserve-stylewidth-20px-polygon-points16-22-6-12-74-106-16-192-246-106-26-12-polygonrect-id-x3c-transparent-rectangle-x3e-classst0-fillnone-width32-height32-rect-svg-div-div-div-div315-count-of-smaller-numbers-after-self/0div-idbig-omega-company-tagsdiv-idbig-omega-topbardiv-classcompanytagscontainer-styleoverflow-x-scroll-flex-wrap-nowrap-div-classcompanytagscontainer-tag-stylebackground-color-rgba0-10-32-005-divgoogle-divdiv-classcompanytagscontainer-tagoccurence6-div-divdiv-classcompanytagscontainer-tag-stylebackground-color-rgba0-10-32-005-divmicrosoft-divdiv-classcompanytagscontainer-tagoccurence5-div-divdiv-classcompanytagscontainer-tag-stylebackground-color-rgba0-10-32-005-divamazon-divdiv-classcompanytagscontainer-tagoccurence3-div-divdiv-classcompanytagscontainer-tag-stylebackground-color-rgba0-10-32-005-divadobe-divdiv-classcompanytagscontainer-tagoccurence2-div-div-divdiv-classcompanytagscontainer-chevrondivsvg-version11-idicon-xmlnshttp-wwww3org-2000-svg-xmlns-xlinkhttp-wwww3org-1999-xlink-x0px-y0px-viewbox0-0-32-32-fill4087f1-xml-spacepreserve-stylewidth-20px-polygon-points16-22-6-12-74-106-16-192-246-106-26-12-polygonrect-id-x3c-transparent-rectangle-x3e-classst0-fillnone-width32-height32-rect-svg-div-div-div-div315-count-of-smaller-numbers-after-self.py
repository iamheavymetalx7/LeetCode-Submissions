class BIT:
    def __init__(self,n):
        self.sums =[0]*(n+1)
    
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
            

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        offset = int(1e4)+1
        
        Fenwick = BIT(2*offset)
        
        def calc_idx(x):
            x+=offset
            return x
        
        ans =[]
        
        for i in reversed(range(len(nums))):
            ans.append(Fenwick.query(calc_idx(nums[i])-1))
            Fenwick.update(calc_idx(nums[i]),1)
        return ans[::-1]
            
            
        
        
        
# class BIT:
#     def __init__(self,n):
#         self.sums = [0]*(n+1)
    
#     def update(self,idx,delta):
#         while idx<len(self.sums):
#             self.sums[idx]+=delta
#             idx+=(idx&(-idx))
        
#     def query(self,idx):
#         s=0
#         while idx>0:
#             s+=self.sums[idx]
#             idx-=(idx&(-idx))
#         return s
# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         n = len(set(nums))
#         dic ={v:i for i,v in enumerate(sorted(set(nums)))}
#         Fenwick = BIT(n)
#         ans =[]
        
#         for i in reversed(range(len(nums))):
#             ans.append(Fenwick.query(dic[nums[i]]+1))
#             Fenwick.update(dic[nums[i]]+1,1)
#         return ans[::-1]