'''
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/2281522/Python-or-90ms-Faster-than-92-or-95-Less-Memory

'''

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        s = sum(nums)
        n=len(nums)
        
        if s%k!=0:
            return False
        
        subset_val = s//k
        
        arr=[0]*(k)
        
        def recur(idx,subset_val):
            if idx==n:
                return True
            
            curr = nums[idx]
            
            for j in range(k):
                if arr[j]+curr<=subset_val:
                    arr[j]+=curr
                    if recur(idx+1,subset_val):
                        return True
                    arr[j]-=curr
                if arr[j]==0:return False
        
        return recur(0,subset_val)
                
                