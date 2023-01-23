from heapq import heappush,heappop,heapify
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # we use priorirty queue, min heap to obtain the ans.
        # we sort num1 on the basis of nums2, from inc to dec such that each time
        # a new element from heap is pused, the minimum elt is current inserted element.
        
        
        # refer: https://leetcode.com/problems/maximum-subsequence-score/discuss/3082106/JavaC%2B%2BPython-Priority-Queue
        
        pq=[]
        total=0
        res=-1
        for b,a in sorted(zip(nums2,nums1),key=lambda x:-x[0]):
            heappush(pq,a)
            total+=a
            
            if len(pq)>k:
                total-=heappop(pq)
                
            if len(pq)==k:
                res=max(res,total*b)
                
        return res

            
                    