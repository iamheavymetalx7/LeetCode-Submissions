'''
https://leetcode.com/problems/combination-sum-iv/discuss/2376043/Striver-Standard-Approach-oror-Recursion-greaterMemoization-greaterTabulation-oror-0-ms

'''

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        @cache
        def recur(tgt):
            if tgt==0:
                return 1
            if tgt<0:
                return 0
            
            ans =0
            for i in range(n):
                if nums[i]<=tgt:
                    ans+=recur(tgt-nums[i])
            return ans
        
        val = recur(target)
        return val
            
            