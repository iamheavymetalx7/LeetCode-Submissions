'''
--> https://leetcode.com/problems/longest-increasing-subsequence-ii/discuss/2561986/Python-Easy-Solution-Well-Explained

--> https://leetcode.com/problems/longest-increasing-subsequence-ii/discuss/2560085/Python-Explanation-with-pictures-Segment-Tree

--> https://leetcode.com/problems/longest-increasing-subsequence-ii/discuss/2578352/Segment-Tree
We just need to make the max range query to run in O(log n) instead of O(n). This can be done using a segment tree.

Note that, for canonical LIS, we can also use the Fenwick tree. With k, Fenwick tree would not work as it can only answer min/max queries on the [0, r] interval (min/max are not commutative operations).

It's possible to use a pair of Fenwick trees to answer mini/max queries on [l, r] interval, but the solution would be much more complicated, compared to a segment tree.
'''
N = 100001
class SegmentTree:
    def __init__(self,N,fn):
        self.N =N
        self.fn=fn
        self.tree=[0]*(2*self.N)
    
    def query(self,l,r):
        l+=self.N
        r+=self.N
        
        res= 0
        while l<r:
            if l&1:
                res=self.fn(res,self.tree[l])
                l+=1    
            if r&1:
                r-=1
                res=self.fn(res,self.tree[r])
            l>>=1
            r>>=1
        return res
    
    def update(self,i,val):
        i+=self.N
        
        self.tree[i]=val
        
        while i>1:
            i>>=1
            self.tree[i]=self.fn(self.tree[2*i],self.tree[2*i+1])
        
        
'''

https://leetcode.com/problems/longest-increasing-subsequence-ii/discuss/2560103/C%2B%2BJava-Segment-Tree-(Max-Range-Query)

'''     

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        
        
        segtree = SegmentTree(N,max)
        res=0
        
        for num in nums:
            lis = segtree.query(max(0,num-k),num)
            lis+=1
            res=max(res,lis)
            segtree.update(num,lis)
        
        return res
        
        