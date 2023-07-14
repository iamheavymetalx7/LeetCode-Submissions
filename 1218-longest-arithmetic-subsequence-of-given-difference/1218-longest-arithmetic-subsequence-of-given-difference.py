class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        res={}
        
        for num in arr:
            res[num] = res.get(num-difference,0)+1
        
        return max(res.values())