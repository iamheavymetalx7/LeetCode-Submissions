'''
https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/discuss/3901622/heapq-union-find-when-SortedlistTreemapordered-Set-**not**-allowed-in-interviews

Sortedlist/Treemap/Set solutions are trivial and useless for real interviews.

use union find. we sort numbers and use union find to quickly identify the nearest neighbors when we loop from right to left.

use heapq. we sort the nums and use heapq when we loop from right to left.
'''
class Solution:
    def minAbsoluteDifference(self, nums: List[int], k: int) -> int:
        
        heap1,heap2=[],[]
        
        if not k:
            return 0
        
        arr=[]
        for i,val in enumerate(nums):
            arr.append([val,i])
        arr.sort()
        res=int(1e11)
        
        for val,idx in arr:
            # print(val,idx)
            
            while heap1 and heap1[0][0]<=idx:
                res=min(res,val-heappop(heap1)[1])
            
            while heap2 and -heap2[0][0]>=idx:
                res=min(res, val-heappop(heap2)[1])
                
                
            heappush(heap1,[idx+k,val]) # min heap
            heappush(heap2,[-(idx-k),val])  # max heap
            # print(heap1, heap2)
        return res