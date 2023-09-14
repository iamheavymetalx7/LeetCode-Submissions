class BIT:
    def __init__(self,n):
        self.sums = [0]*(n+1)
    
    def query(self,idx):
        s=0
        
        while idx>0:
            s+=self.sums[idx]
            idx-=(idx&(-idx))
        return s
    
    def update(self,idx,d):
        while idx<len(self.sums):
            self.sums[idx]+=d
            idx+=(idx&(-idx))

'''
i<j such that
nums1[i]-nums1[j]<=nums2[i]-nums2[j]+diff
nums1[i]-nums2[i]<=num2[i]-nums2[j]+diff
x[i]<=x[j]+diff


'''
            


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        shift = int(3e4)
        mx=int(1e5)
        
        Fenwick = BIT(mx+1)
        res=0
        
        for i in range(len(nums1)):
            k = nums1[i]-nums2[i]
            
            res+=Fenwick.query(k+diff+shift)
            Fenwick.update(k+shift,1)
        return res
            