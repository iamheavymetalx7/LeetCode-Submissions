'''
https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/discuss/1427909/Python-solution-using-LIS-(Longest-Increasing-Subsequence)-concept.

https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/discuss/952053/Python-3-solutions%3A-LIS-dp-O(n-log-n)-explained
'''

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        
        n=len(nums)
        LIS = [1]*(n)
        LDS =[1]*(n)
        
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    LIS[i]=max(LIS[i],1+LIS[j])
        
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if nums[i]>nums[j]:
                    LDS[i]= max(LDS[i],1+LDS[j])
        maxlen =0
        for i in range(n):
            if LIS[i]>1 and LDS[i]>1:
                maxlen=max(maxlen,LIS[i]+LDS[i]-1)

        return n-maxlen